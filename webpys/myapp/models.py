from django.db import models

class Boy(models.Model):
     nickname=models.CharField(max_length=32)
     username= models.CharField(max_length=32)
     password= models.CharField(max_length=32)


class Girl(models.Model):
    nickname= models.CharField(max_length=32)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)


class B2G(models.Model):
     b=models.ForeignKey('Boy',on_delete=models.CASCADE)
     g=models.ForeignKey('Girl',on_delete=models.CASCADE)


class Student(models.Model):
        name=models.CharField(max_length=25,null=True)
        adder=models.CharField(max_length=25,null=True,unique=True)
        age = models.IntegerField(null=True)
        hobby=models.CharField(max_length=22,null=True)
        ctime=models.DateTimeField(auto_now =True)

class User(models.Model):
      username=models.CharField(max_length=25)
      paw=models.IntegerField(null=True)