from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.views.decorators.csrf import  ensure_csrf_cookie
from windstring2016.lottery import *

@ensure_csrf_cookie
def index(request):
    return render(request,'index/index.html')

@login_required(login_url='/')
def lottery(request):
    prizes,candidates,selected=select()
    return render(request,'index/lottery.html',locals())



