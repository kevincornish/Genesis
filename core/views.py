from django.contrib.auth.models import User
from django.contrib.auth import  authenticate
from django.contrib.auth import login as auth_login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from torrents.models import Torrent
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

@login_required(login_url="/login/")
def home(request):
    return render(request, "core/index.html",{})

def doLogin(request):
    if request.method == 'GET':
        return render(request, 'core/login.html')

    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return redirect('login')

def doLogout(request):
    logout(request)
    return redirect('home')

def doSignup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'core/signup.html', {'form': form})

@login_required(login_url="/login/")
def profile(request):
    userprofile = request.user
    torrents = Torrent.objects.filter(uploaded_by__icontains=request.user.username).order_by("-uploaded_at")
    return render(request, 'core/profile.html',{'userprofile':userprofile,'torrents':torrents} )
