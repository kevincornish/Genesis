from django.conf.urls import url, include
from django.contrib import admin
from core import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^login/$', views.doLogin, name='login'),
    url(r'^logout/$',views.doLogout,  name='logout'),
    url(r'^signup/$', views.doSignup, name='signup'),
]