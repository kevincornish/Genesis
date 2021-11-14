from django.contrib import admin
from .models import Torrent,Category

admin.site.register(Category)
admin.site.register(Torrent)