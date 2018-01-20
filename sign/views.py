# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


def index(request):
    # return HttpResponse("Hello Django")
    return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username =='admin' and password=='admin123':
            # return HttpResponse('login success')
            # return render(request,'login.html')
            response = HttpResponseRedirect('/login/')
            response.set_cookie('user',username,3600)
            return response
        else:
            return render(request,'index.html',{'error':'username or password error~'})

def login(request):
    username = request.COOKIES.get('user','')
    return render(request,"login.html",{'user':username})
