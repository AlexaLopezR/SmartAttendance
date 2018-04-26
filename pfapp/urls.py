from django.conf.urls import url
from . import views

urlpatterns= [
	url(r'^$', views.home, name='home'),
    url(r'^profile/$',views.userprofile,name='profile'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.logout,name='login'),
    url(r'^edit/$',views.editprofile,name='edit'),
    url(r'^groups/$',views.groups,name='groups'),
    url(r'^newgroup/$',views.newgroup,name='newgroup'),

]
