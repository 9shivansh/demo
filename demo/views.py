from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from music.views import music_home

# Create your views here.
def index_home(request):

    context = {
        
    }

    return render(request, 'index_home.html', context)


def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:

            login(request, user)
            
            return music_home(request)
            
        else:

            return redirect('error_login')

    context = {

        
    }

    return render(request, 'login_user.html', context)


def register_user(request):

    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index_home.html')

    

    context = {
        'form' : form,

    }

    return render(request, 'register_user.html', context)


def error_login(request):

    return render(request, 'error_login.html')



def logout_user(request):

    logout(request)
    return render(request, 'index_home.html')