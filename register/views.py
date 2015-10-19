from django.shortcuts import render,redirect
from register.forms import RegisterForm
from django.http import  HttpResponseRedirect,JsonResponse
from register.models import Group

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

def auth(request):
    res=dict()
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
        res['status']=1
        res['msg']="登入成功"
    else:
        res['status']=0
        res['msg']="查無資料"
    return JsonResponse(res)


def logout(request):
    request.session['auth']=False
    request.session['email']=None
    request.session['cellphone']=None
    return redirect('/')
