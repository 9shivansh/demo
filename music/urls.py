from django.urls import path
from music import views



urlpatterns = [
    path('', views.music_home, name = 'music_home'),
    path('upload/', views.song_upload, name = 'upload'),
    path('delete/<int:pk>/', views.song_delete, name = 'song_delete'),
]
