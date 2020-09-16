from django.shortcuts import render

# Create your views here.
def music_home(request):

    context = {
        
    }

    return render(request, 'music_home.html', context)