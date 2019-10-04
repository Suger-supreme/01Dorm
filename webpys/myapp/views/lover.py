from django.shortcuts import render,HttpResponse,render_to_response,redirect
from myapp import models

def show(request):
    return  HttpResponse("欢迎来了哈哈哈哈哈哈")

def index(request):
   if not request.session.get("user_info"):
         return redirect("login/")
   else:
       # 男   女生列表
       # 女  男生
     sess_nickname= request.session.get("user_info").get("nickname")   #登录后获取用户名
     print(sess_nickname)
     gender=request.session.get("user_info").get("gender")
     if gender=="1":
          user_list=models.Girl.objects.all()
     else:
          user_list = models.Boy.objects.all()

     # return HttpResponse("111")
     return render(request,"01html/02index.html",{"user_list":user_list,"sess_nickname":sess_nickname})

def other(request):
# 获取当前用户对应的关系
     user_id=request.session.get("user_info").get("user_id")
     gender=request.session.get("user_info").get("gender")
     if gender=="1":
         user_list=models.B2G.objects.filter(b_id=user_id).values("g__nickname")
     else:
         user_list = models.B2G.objects.filter(b_id=user_id).values("b__nickname")
     print(user_list)
     return render(request,"01html/03other.html",{"user_list":user_list})



