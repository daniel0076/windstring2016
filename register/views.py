from django.shortcuts import render,redirect
from register.forms import RegisterForm
from django.http import  HttpResponseRedirect,JsonResponse
from register.models import Group
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

import json


# Create your views here.

def register(request):
    if request.POST:
        form= RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('/')
        else:
            print(form.errors)

    form= RegisterForm()
    return render(request,'register.html',locals())

@login_required(login_url='/')
def view(request):
    competitors=Group.objects.all()
    return render(request,'view.html',locals())

def viewByCat(request,cat):
    categorys=['個人組','團體組','演奏組']
    competitors=Group.objects.filter(category=categorys[int(cat)])
    return render(request,'view.html',locals())

def details(request,query_email=None,query_cellphone=None):
    if request.session.get('auth'):
        query_email=request.session.get('email')
        query_cellphone=request.session.get('cellphone')

    competitors=Group.objects.filter(email=query_email,cellphone=query_cellphone)
    return render(request,'details.html',locals())

def notify(request):
    pass

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


def user_logout(request):
    logout(request)
    request.session['auth']=False
    request.session['email']=None
    request.session['cellphone']=None
    return redirect('/')