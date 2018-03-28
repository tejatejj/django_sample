# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    html_var='my name ia teja'
    #return HttpResponse('hello')
    return render(request,"base.html")
