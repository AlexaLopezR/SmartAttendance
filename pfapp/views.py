from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import UpdateView
from django.contrib import messages

from .forms import UserForm 
from .forms import LoginForm 
from .forms import EditForm 
from .forms import GroupForm 


from .models import Users 
# Create your views here.

def home(request):
	form= LoginForm(request.POST)
	if form.is_valid():
		Email=form.cleaned_data['email']
		Password=form.cleaned_data['password']
		correo=list(Users.objects.values_list('correo',flat=True).filter(correo=Email))
		contra=list(Users.objects.values_list('contrasena',flat=True).filter(contrasena=Password))
		correo=str(correo).replace("['",'')
		contra=str(contra).replace("['",'')
		correo=str(correo).replace("']",'')
		contra=str(contra).replace("']",'')
		contra=str(contra).replace("']",'')
		contra=str(contra).replace("[u'",'')
		correo=str(correo).replace("[u'",'')
		if (correo==Email and Password==contra) :
			request.session['Logged']=True
			request.session['correolog']=Email
			return redirect("profile/")
		else:
			temp=2
			return render(request,'pfapp/login.html',{'message':temp, 'form':form})
	else:
		form=LoginForm()
		try:
			if (request.session['registrado']==1):
				temp=request.session['registrado']
				del request.session['registrado']
				return render(request,'pfapp/login.html',{'message':temp, 'form':form})
		except:
			return render(request,'pfapp/login.html',{'form':form})
		return render(request, 'pfapp/login.html',{'form':form})
	
def register(request):
	if request.method=='POST':
		form=UserForm(request.POST, request.FILES)
		registrado=0
		if form.is_valid():
			form.save()
			registrado=1
			request.session['registrado']=registrado
			return redirect("/")
	else:
		form=UserForm()
		return render(request, 'pfapp/register.html',{'form':form})

def logout (request):
	request.session.flush()
	return redirect("/")

def userprofile(request):
	perfilusuario = Users.objects.filter(correo=request.session['correolog'])
	return render(request,'pfapp/index.html',{'perfilusuario':perfilusuario})

def editprofile(request):
	perfilusuario = Users.objects.filter(correo=request.session['correolog'])
	for i in perfilusuario:
		print(i.nombre)
	if request.method=='POST':
		
		form=EditForm(request.POST, request.FILES,correo=request.session['correolog'], perfil=i) 
		correo=request.session['correolog']
		perfil=i
		if form.is_valid():
			Users.objects.filter(correo=request.session['correolog'])
			pict=Users(id=i.id, correo=correo,
			nombre=form.cleaned_data['nombre'],
			contrasena=form.cleaned_data['contrasena'])
			pict.save()
			return redirect("/profile")

	else:
		form=EditForm(correo=request.session['correolog'], perfil=i)
		return render(request, 'pfapp/edit.html',{'form':form})


def groups(request):
	return render(request, 'pfapp/groups.html')

def newgroup(request):
	if request.method=='POST':
		form=GroupForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect("/groups")
	else:
		form=GroupForm()
		return render(request, 'pfapp/newgroup.html',{'form':form})
	