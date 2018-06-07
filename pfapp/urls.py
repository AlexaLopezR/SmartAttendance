from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth.views import login
from views import register

urlpatterns= [
	#url(r'^$', views.home, name='home'),
    url(r'^profile/$',views.userprofile,name='profile'),
    url(r'^register/$',register.as_view(),name='register'),
    url(r'^login/$',views.logout,name='login'),
    url(r'^edit/$',views.editprofile,name='edit'),
    url(r'^groups/$', views.ProfileList.as_view(), name='profile-list'),
    url(r'^newgroup/$',views.GroupGroupMemberCreate.as_view(),name='GroupGroupMemberCreate'),
    url(r'^$', login, {'template_name': 'pfapp/login.html'}, name='login')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)