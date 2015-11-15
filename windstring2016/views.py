from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import  HttpResponseRedirect
from django.views.decorators.csrf import  ensure_csrf_cookie

@ensure_csrf_cookie
def index(request):
    return render(request,'index/index.html')



