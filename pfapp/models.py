# -*- coding: utf-8 -*-

from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings 
from django.core.validators import validate_comma_separated_integer_list
import os
import numpy 



def get_image_path(instance, filename):
    return os.path.join('pfapp/images/', str(instance.groupid),str(instance.nombreint), filename)

class Users(models.Model):
	nombre= models.CharField(max_length= 80)
	correo= models.EmailField(max_length= 100, unique=False)
	contrasena= models.CharField(max_length=32)

class Group(models.Model):
	group=models.CharField(max_length=80)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.group

	
class GroupMembers(models.Model):
	groupid=models.ForeignKey(Group)
	nombreint= models.CharField(max_length= 80)
	correoint= models.EmailField(max_length= 100, unique=False)
	foto1= models.ImageField(upload_to=get_image_path,default='default.jpg', null= False,blank= False)
	foto2=models.ImageField(upload_to=get_image_path,default='default.jpg', blank= False, null=False)
	cod1= models.TextField()
	cod2= models.TextField(null=True)
	def __str__(self):
		return self.nombreint


class UploadPhoto(models.Model):
	picture1= models.ImageField(upload_to="pfapp/images/",default='default.jpg')
	picture2= models.ImageField(upload_to="pfapp/images/",null=True)

	
class ResultPicture(models.Model):
	result1=models.ImageField(upload_to=get_image_path,default='default.jpg')
	result2=models.ImageField(upload_to=get_image_path,default='default.jpg')
	idgroup=models.ForeignKey(Group, default=1)
	assisted=models.CharField(max_length=1000)
	missing=models.CharField(max_length=1000)
	fecha=models.CharField(max_length=1000)
	idassisted=models.CharField(max_length=1000)
	ratio=models.CharField(max_length=10, null=True)