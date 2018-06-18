# -*- coding: utf-8 -*-

from django import forms
from django.forms.formsets import BaseFormSet
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.models import modelformset_factory
from django.forms.formsets import formset_factory
from django.forms import inlineformset_factory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm , UserChangeForm

from .models import Users, UploadPhoto
from .models import Group
from .models import GroupMembers

class UploadPhotoForm(forms.ModelForm):
	photo = forms.ImageField(label='Agregar Foto 1')
	class Meta:
		model = UploadPhoto
		exclude = ()
		
class UserForm(UserCreationForm):
	
	class Meta:
		model = User
		fields = [ 'username',
					'first_name',
					'last_name',
					'email',
				]
		labels={ 'username': 'Nombre de Usuario',
					'first_name': 'Nombre',
					'last_name': 'Apellidos',
					'email': 'Correo electrónico',
					'password': 'Contraseña'
				}

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'e-mail','style':'width:30%'}))
    password = forms.CharField(label='Contraseña', max_length=32, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'*******','style':'width:30%'}))

class EditForm(UserChangeForm):
	class Meta:
		model = User
		fields = [ 'username',
					'first_name',
					'last_name',
					'email',
					'password'

				]
		labels={ 'username': 'Nombre de Usuario',
					'first_name': 'Nombre',
					'last_name': 'Apellidos',
					'email': 'Correo electrónico',
					'password': 'Contraseña'
				}
	
class GroupMemberForm(forms.ModelForm):
	nombreint= forms.CharField(label='Nombre Completo',max_length= 80, widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:100%'}))
	correoint= forms.EmailField(label= 'Correo', max_length= 100, widget=forms.TextInput(attrs=
                                {'class':'form-control',
                                'placeholder':'example@correo.com',
                                'style':'width:100%'}))
	
	foto1 = forms.ImageField(label='Agregar Foto 1')
	foto2 = forms.ImageField(label='Agregar Foto 2')
	class Meta:
		model = GroupMembers
		exclude = ('cod1', 'cod2')

GroupMemberFormSet = inlineformset_factory(Group, GroupMembers,
                                            form=GroupMemberForm, extra=1)

class UploadPhotoForm(forms.ModelForm):
    picture=forms.ImageField(label='Agregar foto del grupo')
    class Meta:
        model=UploadPhoto
        fields = '__all__'

