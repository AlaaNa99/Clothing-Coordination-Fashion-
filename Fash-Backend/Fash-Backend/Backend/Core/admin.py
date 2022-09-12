from audioop import add
from django.contrib import admin
from .models import UserModel,HomeModel
# Register your models here.
admin.site.register([UserModel,HomeModel])