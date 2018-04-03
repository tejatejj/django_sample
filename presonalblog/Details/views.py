# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    html_var=1000
    num=None
    condition_bool_item=False
    if condition_bool_item:
        num=random.randint(0,190000)
    some_list=[num,html_var,random.randint(0,1200)]
    return render(request,"home.html",{"bool_item":False,"num":num,"some_list":some_list})


def home1(request):
    context={
    }
    return render(request,"home1.html",context)
def about(request):
    context={
    }
    return render(request, "about.html",context)
def contact(request):
    return render(request,"contact.html")
    
