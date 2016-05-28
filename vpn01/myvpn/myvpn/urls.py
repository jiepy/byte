"""myvpn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.shortcuts import render, redirect
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse

def index(request):
    return render(request, template_name='login.html')

def mod_pass(request):
    return render(request, template_name='change_pass.html')


urlpatterns = [
    url(r'^$', index),
    url(r'mod', mod_pass),
    url(r'^admin/', admin.site.urls),
    url(r'^vpn/', include('vadmin.urls')),
]
