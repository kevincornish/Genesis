from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from torrents.forms import TorrentForm
from torrents.models import Torrent, Category
from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

import bencoder

@login_required(login_url="/login/")
def browse(request):
    if 'category' in request.GET:
          category = request.GET.get('category', None)
          if category: 
                torrents = Torrent.objects.filter(category=category)
    else:
        torrents = Torrent.objects.all().order_by("-uploaded_at")
    categories = Category.objects.all()
    return render(request, 'torrents/browse.html',{'torrents':torrents,'categories':categories})

@login_required(login_url="/login/")
def upload(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        fileUploadForm = TorrentForm(request.POST, request.FILES)
        if request.FILES['torrent_path'].name.lower().endswith(('.torrent')):
            if fileUploadForm.is_valid():
                torrentForm = fileUploadForm.save(commit=False)
                torrentForm.torrent_path = request.FILES['torrent_path']
                torrentForm.uploaded_by = request.user.username
                torrentForm.name = request.POST['name']
                torrentForm.category = Category.objects.get(id = request.POST['category'])
                torrentForm.save()
                #lets decode the torrent file and grab what we need    
                with open(torrentForm.torrent_path.path, 'rb') as torrentfile:
                    torrent_bytes = bencoder.decode(torrentfile.read())
                    #print (torrent_bytes)
                return redirect('browse')
        else:
            return HttpResponse("form is not valid")
    else:
        fileUploadForm = TorrentForm()
    return render(request, 'torrents/upload.html', {'form': fileUploadForm,'categories':categories})