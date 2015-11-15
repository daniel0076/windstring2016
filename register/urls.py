"""windstring2016 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from register.views import register,view,details,viewByCat,auth,userLogout,notifyPay,confirmPay
from windstring2016.views import index

urlpatterns = [
    url(r'^$',register,name='register'),
    url(r'^view/$',view,name='view'),
    url(r'^details$',details,name='details'),
    url(r'^logout$',userLogout,name='logout'),
    url(r'^view/(?P<cat>[0-2]+)/$',viewByCat),
    url(r'^auth$',auth,name='auth'),
    url(r'^notify$',notifyPay,name='notify'),
    url(r'^confirm$',confirmPay,name='confirm'),
]
