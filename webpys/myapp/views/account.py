from django.shortcuts import render,HttpResponse,render_to_response,redirect
from myapp import models



def login(request):
  if request.method=="GET":
       return render(request,"01html/01login.html")

  elif  request.method=="POST":

        user=request.POST.get("username")
        pwd=request.POST.get("password")
        rmb=request.POST.get("rmb")
        gender=request.POST.get("gender")

        # 判断性别
        if gender=="1":
            obj=models.Boy.objects.filter(username=user,password=pwd).first()
        else:
            obj = models.Girl.objects.filter(username=user, password=pwd).first()

        if not  obj:  # 未登录成功
             return  render(request,"01html/01login.html",{"msg":"用户密码错误了哈哈哈"})
        else:  # 登录成功
            # request.session["user_id"]=obj.id
            # request.session["gender"]=gender
            # request.session["username"]=user
            request.session["user_info"]={"user_id":obj.id,"gender":gender,"username":user,"nickname":obj.nickname}
            return  redirect("index/")
            # 跳转



def logout(request):
     if request.session.get("user_info"):
           request.session.clear()
     return  redirect("/home/login/")

