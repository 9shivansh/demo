from django.shortcuts import render

# Create your views here.
def index_home(request):

    context = {
        
    }

    return render(request, 'index_home.html', context)