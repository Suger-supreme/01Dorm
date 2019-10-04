from django.shortcuts import render,HttpResponse,render_to_response,redirect
# python manage.py runserver
from myapp import models
from functools import wraps

def text_show(request):
    return HttpResponse("登录成功率")


