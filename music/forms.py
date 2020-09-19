from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SongForm(forms.ModelForm):
    class Meta:
        model = models.song
        fields = ('song_title', 'song_artist', 'song_album', 'song_url', 'song_file')

