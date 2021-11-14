from django.db import models

class Torrent(models.Model):
    name = models.CharField(max_length=255)
    uploaded_by = models.CharField(max_length=25)
    torrent_path = models.FileField(upload_to='torrents/')
    uploaded_at = models.DateTimeField(auto_now=False, auto_now_add=True)
