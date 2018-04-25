from django import forms
from .models import Users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	nombre= forms.CharField(label='Nombre Completo',max_length= 80, widget=forms.TextInput(attrs=
                                {'class':'form-control', 'style':'width:50%'}))
	correo= forms.EmailField(label= 'Email', max_length= 100, widget=forms.TextInput(attrs=
                                {'class':'form-control',
                                'placeholder':'ejemplo@correo.com',
                                'style':'width:50%'}))
	contrasena= forms.CharField(label='Clave', max_length=32, widget=forms.PasswordInput(attrs=
		{
		'class':'form-control', 'placeholder':'Ingrese clave', 'style':'width:50%'
		}))
	

	class Meta:
		model = Users
		fields = '__all__'

class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electronico',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'e-mail','style':'width:30%'}))
    password = forms.CharField(label='Contrasena', max_length=32, widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Clave','style':'width:30%'}))