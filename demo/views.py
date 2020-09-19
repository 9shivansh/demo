from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

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

    context = {
        'form' : UserCreationForm(),

    }

    return render(request, 'register_user.html', context)