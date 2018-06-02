from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns= [
	url(r'^$', views.home, name='home'),
    url(r'^profile/$',views.userprofile,name='profile'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.logout,name='login'),
    url(r'^edit/$',views.editprofile,name='edit'),
    url(r'^groups/$', views.ProfileList.as_view(), name='profile-list'),
    url(r'^newgroup/$',views.GroupGroupMemberCreate.as_view(),name='GroupGroupMemberCreate'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)