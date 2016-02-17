from django.shortcuts import render,redirect
from register.forms import RegisterForm
from django.http import  HttpResponseRedirect,JsonResponse
from register.models import Group
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.mail import send_mail
from django.core import serializers
from django.conf import settings

import json
import xlsxwriter


# Create your views here.

def register(request):
	if request.POST:
		form= RegisterForm(request.POST)
		if form.is_valid():
			#send notify email
			with open(settings.BASE_DIR+"/register/notifyMail.html","r") as f:
				msg=f.read()
			info=request.POST
			to=list()
			to.append(info['email'])
			msg=msg.format(info['contact'],info['category'],info['cellphone'],info['song']
					,info['group_name'],info['mic'],info['mic_holder'],info['chair'])
			send_mail('感謝你報名2016風弦盃，請確認報名資訊', 'Here is the message.', '交通大學風弦盃 <windstring@guitar.nctu.me>',
				to,html_message=msg, fail_silently=False)

			user=form.save()
			query_email=request.POST.get('email')
			query_cellphone=request.POST.get('cellphone')
			request.session['auth']=True
			request.session['email']=query_email
			request.session['cellphone']=query_cellphone
			return redirect('/register/details')
		else:
			print(form.errors)


	form= RegisterForm()
	return render(request,'register.html',locals())

@login_required(login_url='/')
def view(request):
	competitors=Group.objects.all()
	title="所有組別"
	return render(request,'view.html',locals())

@login_required(login_url='/')
def deleteItem(request):
	if request.body:
		data=request.body.decode()
		gid=json.loads(data).get('gid')
		item=Group.objects.get(gid=gid)
		if item:
			item.delete()
			return JsonResponse({'success':True})
	else:
		return JsonResponse({'success':False})

@login_required(login_url='/')
def viewByCat(request,cat):
	categorys=['個人組','團體組','演奏組']
	competitors=Group.objects.filter(category=categorys[int(cat)])
	title=categorys[int(cat)]
	return render(request,'view.html',locals())

def details(request,query_email=None,query_cellphone=None):
	if request.session.get('auth'):
		query_email=request.session.get('email')
		query_cellphone=request.session.get('cellphone')

	competitors=Group.objects.filter(email=query_email,cellphone=query_cellphone)
	return render(request,'details.html',locals())

@ensure_csrf_cookie
def notifyPay(request):
	if request.body:
		data=request.body.decode()
		gid=json.loads(data).get('gid')
		user_email=request.session.get('email')
		user_cellphone=request.session.get('cellphone')
		notify_item=Group.objects.get(gid=gid,email=user_email,cellphone=user_cellphone)
		if notify_item and request.session.get('auth'):
			notify_item.pay_status=1
			notify_item.save()
			return JsonResponse({'success':True})
	else:
		return JsonResponse({'success':False})

@ensure_csrf_cookie
def confirmPay(request):
	if request.body:
		data=request.body.decode()
		gid=json.loads(data).get('gid')
		notify_item=Group.objects.get(gid=gid)
		if notify_item and request.user.is_authenticated():
			notify_item.pay_status=2
			notify_item.save()
			return JsonResponse({'success':True})
	else:
		return JsonResponse({'success':False})

@ensure_csrf_cookie
def auth(request):
	res=dict()
	res['msg']="查無資料"
	res['success']=0
	request.session['auth']=False
	request.session['email']=None
	request.session['cellphone']=None

	if request.body:
		req=request.body.decode()
		query_email=json.loads(req).get('email')
		query_cellphone=json.loads(req).get('cellphone')
		auth=Group.objects.filter(email=query_email,cellphone=query_cellphone)
	else:
		auth=False
	if auth:
		request.session['auth']=True
		request.session['email']=query_email
		request.session['cellphone']=query_cellphone
		res['msg']="選手登入成功"
		res['success']=1
		res['rdr']="/register/details"
	else:
		user = authenticate(username=query_email, password=query_cellphone)
		if user is not None:
			if user.is_active:
				login(request,user)
				request.session['auth']=True
				request.session['email']=query_email
				request.session['cellphone']=query_cellphone
				res['msg']="管理員登入成功"
				res['success']=1
				res['rdr']="/register/view"
			else:
				res['msg']="帳號鎖定"

	return JsonResponse(res)


def userLogout(request):
	logout(request)
	request.session['auth']=False
	request.session['email']=None
	request.session['cellphone']=None
	return redirect('/')

@login_required
def send_email(request):

		#send_mail('歡迎參加2016年 交通大學 風弦盃吉他比賽', 'Here is the message.', '交通大學風弦盃 <windstring@guitar.nctu.me>',
		#	tmp,html_message=msg, fail_silently=False)
	return render(request,'mailing.html',locals())


@login_required
def exportExcel(request):
	workbook = xlsxwriter.Workbook(settings.BASE_DIR+"/static/files/匯出.xlsx")
	worksheet = workbook.add_worksheet()
	competitors=Group.objects.all().order_by('category')
	json_data= json.loads(serializers.serialize('json', competitors))
	row=1
	worksheet.write(0,0,'組別')
	worksheet.write(0,1,'姓名')
	worksheet.write(0,2,'手機')
	worksheet.write(0,3,'麥克風數')
	worksheet.write(0,4,'麥架數')
	worksheet.write(0,5,'椅子數')
	worksheet.write(0,6,'初賽歌名')
	worksheet.write(0,7,'email')
	worksheet.write(0,8,'付款狀態')
	worksheet.write(0,9,'Facebook')
	worksheet.write(0,10,'團名')
	worksheet.write(0,11,'隊員1')
	worksheet.write(0,12,'隊員2')
	worksheet.write(0,13,'隊員3')
	worksheet.write(0,14,'隊員4')
	worksheet.write(0,15,'隊員5')
	worksheet.write(0,16,'隊員6')
	worksheet.write(0,17,'隊員7')
	worksheet.write(0,18,'備註')
	for item in json_data:
		worksheet.write(row,0,item['fields']['category'])
		worksheet.write(row,1,item['fields']['contact'])
		worksheet.write(row,2,item['fields']['cellphone'])
		worksheet.write(row,3,item['fields']['mic'])
		worksheet.write(row,4,item['fields']['mic_holder'])
		worksheet.write(row,5,item['fields']['chair'])
		worksheet.write(row,6,item['fields']['song'])
		worksheet.write(row,7,item['fields']['email'])
		worksheet.write(row,8,item['fields']['pay_status'])
		worksheet.write(row,9,item['fields']['fb_url'])
		worksheet.write(row,10,item['fields']['group_name'])
		worksheet.write(row,11,item['fields']['player1'])
		worksheet.write(row,12,item['fields']['player2'])
		worksheet.write(row,13,item['fields']['player3'])
		worksheet.write(row,14,item['fields']['player4'])
		worksheet.write(row,15,item['fields']['player5'])
		worksheet.write(row,16,item['fields']['player6'])
		worksheet.write(row,17,item['fields']['player7'])
		worksheet.write(row,18,item['fields']['ps'])
		row+=1

	workbook.close()
	return redirect("/static/files/匯出.xlsx")

