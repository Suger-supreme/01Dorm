from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("这是django欢迎来到首页哈哈哈哈！！！！")
