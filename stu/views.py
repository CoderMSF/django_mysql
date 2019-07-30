# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import *


def index_view(request):

    m = request.method

    if m == 'GET':
        return render(request, 'register.html')
    else:
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd', '')

        if uname and pwd:
            stu = Student(sname=uname, spwd=pwd)
            stu.save()



        return HttpResponse('register success')

    return HttpResponse('register false')


def show_view(request):
    stus = Student.objects.all()
    return render(request, 'show.html', {'students':stus})



