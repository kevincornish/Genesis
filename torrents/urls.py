from django.conf.urls import url, include
from django.contrib import admin
from torrents import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^browse/$', views.browse, name='browse'),
]