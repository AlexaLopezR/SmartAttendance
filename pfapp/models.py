from django.contrib.auth import get_user_model

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings 
import os


def get_image_path(instance, filename):
    return os.path.join('pfapp/images/', str(instance.group),str(instance.nombreint), filename)

class Users(models.Model):
	nombre= models.CharField(max_length= 80)
	correo= models.EmailField(max_length= 100, unique=True)
	contrasena= models.CharField(max_length=32)

class Group(models.Model):
	grupo=models.CharField(max_length=80)
	user=models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.grupo

	
class GroupMembers(models.Model):
	group=models.ForeignKey(Group)
	nombreint= models.CharField(max_length= 80)
	correoint= models.EmailField(max_length= 100, unique=True)
	foto1= models.ImageField(upload_to=get_image_path,default='default.jpg')
	foto2=models.ImageField(upload_to=get_image_path,default='default.jpg')
	def __str__(self):
		return self.nombreint


class UploadPhoto(models.Model):
	fotogrupo= models.ImageField(upload_to="pfapp/images/",default='default.jpg')



	