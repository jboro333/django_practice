from django.conf.urls import url
from django.contrib.auth import login_required

from rest_framework.urlpatterns import format_suffix_patters

from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from model import Playlist, Song, Album, Artist
from forms import SongForm, PlaylistForm, AlbumForm, ArtistForm
from views import SongDetail, SongCreate, AlbumDetail, AlbumCreate, \
    PlaylistDetail, PlaylistCreate, ArtistDetail, ArtistCreate, Register


urlpatterns = [
    url(r'^register', Register.as_view(), name='register')
]
"""
    url(r'^$',
        ListView.as_view(
            queryset=Song.objects.filter(date__lte=timezone.now()).order_by('-d
                ate')[:5],
            context_object_name='latest_restaurant_list',
            template_name='myrestaurants/restaurant_list.html'),
        name='restaurant_list')
]
"""
