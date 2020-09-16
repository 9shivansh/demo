from django.urls import path
from music import views



urlpatterns = [
    path('', views.music_home, name = 'music_home'),
]
