from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect, HttpResponse

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
from .datos import *
from .forms import * 
from .models import *


# Create your views here.
class register(CreateView): #Vista para el registro de usuario
	"""docstring for register"""
	model = User
	template_name= "pfapp/register.html"
	form_class = UserForm

	success_url=reverse_lazy('login')
	

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
	template_name = 'group_list.html'
	def get_queryset(self):
		return Group.objects.filter(user_id=self.request.user)
	
class GroupGroupMemberCreate(CreateView): #Vista para el formulario del grupo
	model = Group
	fields = ['group']
	labels= {'grupo': 'Group Name' }
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
			form.instance.user = self.request.user
      		self.object = form.save()	
      		if groupmembers.is_valid():
      			groupmembers.instance = self.object
      			groupmembers.save()
		return super(GroupGroupMemberCreate, self).form_valid(form)
	  

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
	for p in GroupMembers.objects.raw('SELECT * FROM pfapp_groupmembers WHERE  groupid_id=( SELECT MAX(groupid_id) FROM pfapp_groupmembers )'):
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
		GroupMembers.objects.filter(id =pk[i]).update(cod1 =cod[0])
	for i in range(0,len(y)):
		image = face_recognition.load_image_file(y[i])
		cod=face_recognition.face_encodings(image)
		cod=np.array(cod)
		print(type(cod))
		GroupMembers.objects.filter(id =pk[i]).update(cod2 =cod[0])
		

	print("listo")
	return redirect('profile-list')
grupo_selec=0
def GroupList(request, group_grupo): #Vista para ver los integrantes del grupo
	query_group=GroupMembers.objects.filter(groupid=group_grupo)
	global grupo_selec
	grupo_selec=group_grupo
	context={
	'query_group':query_group
	}
	return render(request,'pfapp/lista.html',context)
			
class GroupPhotoEntry(CreateView): #Vista para cargar foto de asistencia
 
	model = UploadPhoto
	template_name= "pfapp/uploadphoto_form.html"
	form_class = UploadPhotoForm
	success_url=reverse_lazy('attendance')

def attendanceGenerator(request): #Vista para generar asistencia
	from os import listdir
	import os
	from os.path import join
	import pickle
	from PIL import Image, ImageFont,  ImageDraw,ImageEnhance
	import face_recognition
	from face_recognition import face_locations
	from face_recognition.cli import image_files_in_folder
	import cv2 
	from resizeimage import resizeimage
	import numpy as np
	import MySQLdb
	bd= MySQLdb.connect("127.0.0.1","root", "123pf","PF")
	cursor = bd.cursor()
	global grupo_selec

	cursor.execute("SELECT id,cod1, cod2 FROM pfapp_groupmembers WHERE groupid_id = '%s'" %grupo_selec)
	results = cursor.fetchall()
	A = np.array([])
	for i in results:
		A = np.append(A, i[1])
		A= np.append(A, i[2])
	A=','.join(map(str, A)) 
	A=A.replace(' ',',')
	A=A.replace(',,,',',')
	A=A.replace(',,',',')
	A=A.replace(',,',',')
	print("Tipo de A")
	A=eval(A)
	A = [np.array(element) for element in A]
	known_face_encodings=A
	
	B = np.array([])
	for n in GroupMembers.objects.raw('SELECT id, nombreint FROM pfapp_groupmembers WHERE groupid_id = %s', [grupo_selec]):
		name=n.nombreint
		list_string = str(name)
		name=np.array(list_string)
		B = np.append(B, name)
		B = np.append(B, name)
	B=','.join(map(str, B))
	B=B.split(',')
	known_face_names=B

	tol=0.6
	for p in UploadPhoto.objects.raw('SELECT * FROM pfapp_uploadphoto WHERE  id=( SELECT MAX(id) FROM pfapp_uploadphoto )'):
		dire1=os.path.join('/home/alexalopez/PF/SmartAttendance/static/media/', str(p.picture))
		unknown_image = face_recognition.load_image_file(dire1)
		image=Image.fromarray(unknown_image)
		enhancer_object = ImageEnhance.Contrast(image)
		enhancer_object = ImageEnhance.Color(image)
		out = enhancer_object.enhance(1.3)
		out.save('/home/alexalopez/PF/SmartAttendance/static/media/imagenmejorada.jpg')
		unknown_image = face_recognition.load_image_file('/home/alexalopez/PF/SmartAttendance/static/media/imagenmejorada.jpg')
		height = np.size(unknown_image, 0)
		width = np.size(unknown_image, 1)
		if (width<2000 and height<2000):
			unknown_image = cv2.resize(unknown_image, (2500, 2000)) 
		face_locations = face_recognition.face_locations(unknown_image, number_of_times_to_upsample=0, model="cnn")
		face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
		pil_image = Image.fromarray(unknown_image)

		#  Create a Pillow ImageDraw Draw instance to draw with
		draw = ImageDraw.Draw(pil_image)
		# Loop through each face found in the unknown image
		for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
		# See if the face is a match for the known face(s)
			matches = face_recognition.face_distance(known_face_encodings, face_encoding)
			name = "Unknown"
			if(min(matches)<=tol):
				mindispos = matches.tolist().index(min(matches))
				name = known_face_names[mindispos]
		 # Draw a box around the face using the Pillow module
			draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

		 # Draw a label with a name below the face
			text_width, text_height = draw.textsize(name)
			draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
			draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


		 # Remove the drawing library from memory as per the Pillow docs
		del draw

		 #  Display the resulting image
		pil_image.save("resultado_salon.jpg")

	
	html = "<html><body>It is now.</body></html>"
	return HttpResponse(html)
	
	
def loadExcel(request):

	if request.method == 'POST':
		form = ExcelUpload(request.POST, request.FILES)
		if form.is_valid():
			#Get File from the form
			ExcelFile=request.FILES['ExcelFile']
			#Validating File
			if ExcelFile.name.find(".xls")==-1:
				print("NO EXCEL FILE")
				messages.add_message(request, messages.ERROR,"Choose a file (.xls o .xlsx)")
				return redirect("/loadexcel")
			#Saving the excel file
			rootpath=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Excel')
			fs=FileSystemStorage(location=rootpath)
			#delete de file if exist
			fs.delete(ExcelFile.name)
			filename=fs.save(ExcelFile.name,ExcelFile)
			sheetnames=Sheets(ExcelFile.name)
			#Saving Sessions
			request.session['sheetnames']=sheetnames
			request.session['ExcelName']=ExcelFile.name
			request.session['Uploaded']=True
			#request.session['user']='UsuarioPruebas'
			
			return redirect("/chooseSheet")
	else:
		form = ExcelUpload()
		#Deleting a file that will not be used
	try:
		if request.session['Uploaded']:
				rootpath=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'Excel')
				fs=FileSystemStorage(location=rootpath)
				fs.delete(request.session['ExcelName'])
	except:
		print('Not File')
	request.session['Uploaded']=False
	return render(request,'pfapp/excelform.html',{'form':form})
	
def chooseSheet(request):
	if request.method=='POST':
		form=SheetSelection(request.POST, sheetlist=request.session['sheetnames'])
		if form.is_valid():
			#getting data from the form and Saving sessions to use it later
			sheet=form.cleaned_data['sheets']
			request.session['sheet']=sheet
			
			return redirect("/pickColumns")
	else:
		form=SheetSelection(sheetlist=request.session['sheetnames'])
	return render(request,'pfapp/sheet_form.html',{'form':form})

def pickcolumns(request):

	columnslist,ExcelFile=Columns(request.session['ExcelName'],request.session['sheet'])
	form=ColumnsSelection(columnslist=columnslist)
	#Replacing NaN for ""
	ExcelFile=ExcelFile.replace(pd.np.nan,'', regex=True)
	#Showing all rows Excel file
	ExcelFile=ExcelFile.to_html(classes='table-striped " id = "my_table',index=False)
	if request.method=='POST':
		form=ColumnsSelection(request.POST  ,columnslist=columnslist)
		#get selection
		if form.is_valid():
			columns=form.cleaned_data['columns']
			request.session['columns']=columns
			
			return redirect('/formset_excel')
		else:
			#Looking for error messages 
			if form.errors.as_data():
				for e in form.errors['columns'].as_data():
					e=str(e)
					e=e[2:len(e)-2]
					messages.add_message(request, messages.ERROR,e)
	return render(request,'pfapp/pickcolumns.html',{'form':form,'ExcelFile':ExcelFile})

class formset_excel(CreateView):
	
	model = Group
	fields = ['group']
	template_name= "pfapp/group_excel_form.html"

	success_url = reverse_lazy('photo')
	def get_context_data(self, **kwargs):
		#Vector con datos de nombres
		nombres=['juan','jose']
		#create Formset
		GroupMemberExcelFormSet = inlineformset_factory(Group, GroupMembers,
                                            form=GroupMemberForm, extra=len(nombres))
		data = super(formset_excel, self).get_context_data(**kwargs)

		if self.request.POST:
			data['groupmembers'] = GroupMemberExcelFormSet(self.request.POST, self.request.FILES)
		else:
			data['groupmembers'] = GroupMemberExcelFormSet(initial=[{'nombreint': nombres[i]} for i in range(0,len(nombres))])

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
		return super(formset_excel, self).form_valid(form)
		
