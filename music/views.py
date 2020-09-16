from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import SongForm
from music import models


#from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def song_upload(request):
    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('music_home')
    else:
        form = SongForm()
    context = {
        'form' : form
    }
    return render(request, 'upload.html', context)

# Create your views here.
def music_home(request):

    all_objs = models.song.objects.all()

    context = {
        'all_objs' : all_objs,
    }

    return render(request, 'music_home.html', context)
