from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import SongForm
from music import models
from django.views.generic import TemplateView, ListView
from django.db.models import Q


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
    return render(request, 'upload_music.html', context)

# Create your views here.
def music_home(request):

    all_objs = models.song.objects.all()
    print(all_objs)
    
    context = {
        'all_objs' : all_objs,
    }

    return render(request, 'music_home.html', context)


def song_delete(request, pk):

    to_be_deleted = models.song.objects.get(id = pk)

    to_be_deleted.delete()

    return redirect('music_home')

class SearchResultsView(ListView):
    model = models.song
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = models.song.objects.filter(
            Q(song_title__icontains=query) | Q(song_artist__icontains=query)
        )
        return object_list