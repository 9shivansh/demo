from django.db import models

# Create your models here.
class song(models.Model):

    song_title = models.TextField(max_length = '250')
    song_artist = models.TextField(max_length = '100')
    song_album = models.TextField(max_length = '100')
    song_url = models.TextField(max_length = '500')

    def __str__(self):

        return self.song_title + ' by ' + self.song_artist + ' from the album - ' + self.song_album