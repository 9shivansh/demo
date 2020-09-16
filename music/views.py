from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.core.files.storage import FileSystemStorage


#from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'upload.html')

# Create your views here.
def music_home(request):

    context = {

    }

    return render(request, 'music_home.html', context)