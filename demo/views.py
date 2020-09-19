from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

# Create your views here.
def index_home(request):

    context = {
        
    }

    return render(request, 'index_home.html', context)


def login_user(request):


    context = {
        
    }

    return render(request, 'login_user.html', context)


def register_user(request):

    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('music_home')

    

    context = {
        'form' : form,

    }

    return render(request, 'register_user.html', context)