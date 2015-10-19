from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import  HttpResponseRedirect

def index(request):
    return render(request,'index/index.html')



