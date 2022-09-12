import os
from django.db import models
from uuid import uuid4

def upload_to(ins,filename):
    return f"{os.path.join('Images',str(ins.USERID),filename)}"

class UserModel(models.Model):
    USERID = models.UUIDField(default=uuid4)
    Username = models.CharField(max_length=200,blank=False,null=False,unique=True)
    Password = models.CharField(max_length=255,blank=False,null=False)
    Age = models.IntegerField(null=True,blank=True)
    Gender = models.CharField(max_length=10,blank=True,null=True)
    SkinColor = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self) -> str:
        return self.Username+ " " + str(self.USERID)
    
class HomeModel(models.Model):
    USERID = models.UUIDField(blank=False,null=False)
    Season = models.CharField(max_length=255, blank=True, null=True)
    ClotheName = models.CharField(max_length=255,blank=True,null=True)
    Type = models.CharField(max_length=255,blank=True,null=True)
    Color = models.CharField(max_length=255,blank=True,null=True)
    Image = models.ImageField(upload_to = upload_to)

class FirstScreenModel(models.Model):
    USERID = models.UUIDField(blank=False, null=False)
    Occasion = models.CharField(max_length=255, blank=True, null=True)
    PersonType = models.CharField(max_length=255, blank=True, null=True)


class SecondScreenModel(models.Model):
    USERID = models.UUIDField(blank=False, null=False)
    Occasion = models.CharField(max_length=255, blank=True, null=True)
    PersonType = models.CharField(max_length=255, blank=True, null=True)
    ClotheName = models.CharField(max_length=255, blank=True, null=True)
    Type = models.CharField(max_length=255, blank=True, null=True)
    Color = models.CharField(max_length=255, blank=True, null=True)


class ThirdScreenModel(models.Model):
    USERID = models.UUIDField(blank=False, null=False)
    Occasion = models.CharField(max_length=255, blank=True, null=True)
    PersonType = models.CharField(max_length=255, blank=True, null=True)
    Image = models.ImageField(upload_to=upload_to)

class Output(models.Model):
    USERID = models.UUIDField(blank=False, null=False)
    pathImage = models.CharField(max_length=1000, blank=True, null=True)
    resultid = models.CharField(max_length=1000, blank=True, null=True)
