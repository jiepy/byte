from .models import Check
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return HttpResponse('This is vadmin Page .')


def check(request):
    username = request.POST.get('username')
    passwd = request.POST.get('password')
    try:
        ucheck = Check(username, passwd)
        if ucheck.has_user == 1 and ucheck.check_pass == 3:
            # auth success.
            return HttpResponse(1)
        elif ucheck.has_user == 0 or ucheck.check_pass == 4:
            # username / passwd error
            return HttpResponse(0)
        else:
            return HttpResponse('nouser')
    except Exception as e:
        return HttpResponse(e)

def userpage(request):
    if not request.user.is_authenticated():
        return HttpResponse('<br />'.join(dir(request.user)))
    return render(request, template_name='chanage_pass.html', context={'user': request.user.username.strip()})


