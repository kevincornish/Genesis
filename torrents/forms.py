from django import forms
from .models import Torrent

class TorrentForm(forms.ModelForm):
    class Meta:
        model = Torrent
        fields = ('torrent_path','name')