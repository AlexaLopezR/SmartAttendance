# -*- coding: utf-8 -*-

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Users
from .models import Groups

class UserForm(forms.ModelForm):
	nombre= forms.CharField(label='Nombre Completo',max_length= 80, widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:50%'}))
	correo= forms.EmailField(label= 'Correo electrónico', max_length= 100, widget=forms.TextInput(attrs=
                                {'class':'form-control',
                                'placeholder':'ejemplo@correo.com',
                                'style':'width:50%'}))
	contrasena= forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput(attrs=
		{
		'class':'form-control', 'placeholder':'Mínimo 6 caracteres', 'style':'width:50%'
		}))
	

	class Meta:
		model = Users
		fields = '__all__'

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'e-mail','style':'width:30%'}))
    password = forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'*******','style':'width:30%'}))

class EditForm(forms.ModelForm):
	nombre= forms.CharField(label='Nombre Completo',max_length= 80, widget=forms.TextInput(attrs=
                               {'class':'form-control', 'style':'width:30%'}))
	contrasena= forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput(attrs=
		{
		'class':'form-control', 'placeholder':'Mínimo 6 caracteres', 'style':'width:30%'
		}))

	class Meta:
		model = Users
		fields = ('nombre', 'contrasena',)

class GroupForm(forms.ModelForm):
	nombregrupo= forms.CharField(label='Identificación del grupo',max_length= 80, widget=forms.TextInput(attrs=
                               {'class':'form-control', 'style':'width:50%'}))
	fechainicio= forms.DateField(label= 'Fecha inicio de actividad', widget=forms.DateInput(format=('%m-%d-%Y'), 
                               attrs={'class':'form-control','style':'width:50%', 
							   'placeholder':'m-d-a'}))
	horainicio=forms.TimeField(label= 'Hora de inicio de actividad', widget=forms.DateInput( 
                               attrs={'class':'form-control','style':'width:50%', 
							   'placeholder':'hh:mm'}))

	class Meta:
		model = Groups
		fields = '__all__'


