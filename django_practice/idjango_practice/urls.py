from django.conf.urls import url, include
from django.contrib.auth import login_required

from rest_framework.urlpatterns import format_suffix_patters
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from model import Playlist, Song, Album, Artist
from forms import SongForm, PlaylistForm, AlbumForm, ArtistForm
from . import views
from accounts.views import (login_view, register_view, logout_view)

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', views.Login),

    # url(r'^register', Register.as_view(), name='register'),
    # url(r'^accounts/', include('registration.backends.default.urls'))
]
