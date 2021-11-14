from django.contrib import admin
from .models import Torrent,Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register( Category, CategoryAdmin)

class TorrentAdmin(admin.ModelAdmin):
    list_display = ['name','category']

admin.site.register( Torrent, TorrentAdmin)