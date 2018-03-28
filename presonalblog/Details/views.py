# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    html_var=1000
    num=random.randint(0,190000)
    some_list=[num,html_var,random.randint(0,1200)]
    return render(request,"base.html",{"bool_item":False,"num":num,"some_list":some_list})



