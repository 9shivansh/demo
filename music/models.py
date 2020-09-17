from django.db import models
from django.urls import reverse

# Create your models here.
class song(models.Model):

    song_title = models.CharField(max_length = 100)
    song_artist = models.CharField(max_length = 100)
    song_album = models.CharField(max_length = 100)
    song_url = models.CharField(max_length = 100)
    song_file = models.FileField(upload_to='music/mp3', default=None)

    def __str__(self):

        return self.song_title + ' by ' + self.song_artist + ' from the album - ' + self.song_album


    def delete(self, *args, **kwargs):

        self.song_file.delete()
        super().delete(*args, **kwargs)