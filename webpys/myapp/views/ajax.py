from django.shortcuts import render,HttpResponse,render_to_response,redirect
import os
from django.conf import settings
from myapp import models

def ajax_show(request):

  if request.method=="GET":
      stu_list=models.Student.objects.all()
      return render(request,"01html/04ajax_show.html",{"student":stu_list})


  elif request.method == "POST":
         nid=request.POST.get("nid")
         models.Student.objects.filter(id=nid).delete()
         return HttpResponse("删除成功了哈哈哈哈")





