from django.shortcuts import render, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import UpdateView
from django.contrib import messages
from django.db import IntegrityError, transaction
from django.forms.formsets import formset_factory
from django.core.urlresolvers import reverse_lazy 
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.conf import settings 
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.hashers import PBKDF2PasswordHasher
import time

from .forms import UserForm 
from .forms import LoginForm 
from .forms import EditForm, UploadPhotoForm
from .forms import GroupMemberFormSet

from .models import Users
from .models import Group
from .models import GroupMembers
from .models import UploadPhoto


# Create your views here.

class register(CreateView): #Vista para el registro de usuario
	"""docstring for register"""
	model = User
	template_name= "pfapp/register.html"
	form_class = UserForm
	success_url=reverse_lazy('')


def logout (request): #Vista para cerrar sesion
	request.session.flush()
	return redirect("/")

def userprofile(request):
	current_user= request.user
	return render(request,'pfapp/index.html')

def editprofile(request): #Vista para editar perfil de usuario 
	if request.method == "POST":
		form=EditForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('/profile/')
	else:
		form=EditForm(instance=request.user)
		return render(request, 'pfapp/edit.html',{'form':form})

def change_password(request): #Vista para cambiar clave de usuario
	if request.method == "POST":
		form=PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request,form.user)
			return redirect('/profile/')
		else:
			return redirect('/edit/')
	else:
		form=PasswordChangeForm(user=request.user)
		return render(request, 'pfapp/changepassword.html',{'form':form})


class ProfileList(ListView): #Vista para ver los grupos creados
	model = Group
	
class GroupGroupMemberCreate(CreateView): #Vista para el formulario del grupo

    model = Group
    fields = ['grupo']
    success_url = reverse_lazy('photo')
    def get_context_data(self, **kwargs):
        data = super(GroupGroupMemberCreate, self).get_context_data(**kwargs)

        if self.request.POST:
        	data['groupmembers'] = GroupMemberFormSet(self.request.POST, self.request.FILES)
        else:
            data['groupmembers'] = GroupMemberFormSet()
        return data
    def form_valid(self, form):
        context = self.get_context_data()      
        groupmembers = context['groupmembers']
        with transaction.atomic():
      		#changing value
        	form.instance.user = self.request.user
        	self.object = form.save()	
        	if groupmembers.is_valid():
        		groupmembers.instance = self.object
        		groupmembers.save()
       	return super(GroupGroupMemberCreate, self).form_valid(form)
  
class GroupPhotoEntry(CreateView):
	model = UploadPhoto
	template_name= "pfapp/uploadphoto_form.html"
	form_class = UploadPhotoForm
	success_url=reverse_lazy('')	

def codificacion(request): #Vista para obtener el vector con las caracteristicas de las personas
	from os import listdir
	from os.path import join
	import face_recognition
	from face_recognition import face_locations
	from face_recognition.cli import image_files_in_folder
	import os
	import numpy as np

	x=[]
	y=[]
	pk=[]
	for p in GroupMembers.objects.raw('SELECT * FROM pfapp_groupmembers WHERE  group_id=( SELECT MAX(group_id) FROM pfapp_groupmembers )'):
		dire1=os.path.join('/home/alexalopez/PF/SmartAttendance/static/media/', str(p.foto1))
		dire2=os.path.join('/home/alexalopez/PF/SmartAttendance/static/media/', str(p.foto2))
		x.append(dire1)
		y.append(dire2)
		pk.append(p.id)
	for i in range(0,len(x)):
		image = face_recognition.load_image_file(x[i])
		cod=face_recognition.face_encodings(image)
		cod=np.array(cod)
		print(type(cod))
		GroupMembers.objects.filter(id =pk[i]).update(cod1 =cod)
	for i in range(0,len(y)):
		image = face_recognition.load_image_file(y[i])
		cod=face_recognition.face_encodings(image)
		cod=np.array(cod)
		print(type(cod))
		GroupMembers.objects.filter(id =pk[i]).update(cod2 =cod)
		

	print("listo")
	return redirect('profile-list')

def GroupList(request, group_grupo): #Vista para ver los integrantes del grupo
	query_group=GroupMembers.objects.filter(group=group_grupo)
	print(query_group)
	context={
	'query_group':query_group
	}
	return render(request,'pfapp/lista.html',context)
    		

