from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Users(models.Model):
	nombre= models.CharField(max_length= 80)
	correo= models.EmailField(max_length= 100, unique=True)
	contrasena= models.CharField(max_length=32)
	
class Groups(models.Model):
	nombregrupo=models.CharField(max_length=80)
	