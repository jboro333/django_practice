"""django_practice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from idjango_practice import views
from django.views.generic import DetailView, ListView, UpdateView
from rest_framework.urlpatterns import format_suffix_patterns

from django.views.generic import View, RedirectView
from idjango_practice.views import *
from idjango_practice.forms import *
from idjango_practice.models import *
from idjango_practice.serializers import *

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^home/$', views.home, name="home"),
    # url(r'^login/', login_view, name="login"),
    # url(r'^logout/', logout, name="logout"),
    url(r'^admin/', admin.site.urls),
    url(r'^contact', views.contact, name="contact"),
    # url(r'^accounts/login/$', login, name='login'),
    # url(r'^accounts/logout/$', logout, name='logout'),
    # url(r'^register/$', views.UserFormView, name="register"),
    # url(r'^artist', ArtistDetail, name="artist"),
    # url(r'^song', views.SongCreate, name="song"),
    # url(r'^album', views.album, name="album"),
    # url(r'^playlist', views.playlist, name="playlist"),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # List all artists: /Aplicacio/teams/
    # url(r'^artist/list/$', ArtistList.as_view(), name='artist_list'),
    url(r'^artist/create/$', ArtistCreate.as_view(), name='artist_create'),
    # url(r'^song/list/$', SongList.as_view(), name='song_list'),
    url(r'^song/create', SongCreate.as_view(), name="song_create"),
    # url(r'^album/list$', AlbumList.as_view(), name="album_list"),
    url(r'^album/create$', AlbumCreate.as_view(), name="album_create"),
    # url(r'^playlist/list$', PlaylistList.as_view(), name="playlist_list"),
    url(r'^playlist/create', PlaylistCreate.as_view(), name="playlist_create"),
    url(r'^artist/(?P<pk>\d+)/$', ArtistDetail.as_view(), name='artist_detail'),
    url(r'^song/$', SongDetail.as_view(), name="song_detail"),
    url(r'^album/$', AlbumDetail.as_view(), name="album_detail"),
    url(r'^playlist/$', PlaylistDetail.as_view(), name="playlist_detail"),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # url(r'^login', views.login, name="login"),
    # url(r'^accounts/', include('registration.backends.default.urls'))

    url(r'^artists/$',
        ListView.as_view(
            queryset=Artist.objects.all,
            context_object_name='artist_list',
            template_name='artist_list.html'),
        name='artist_list'),
    url(r'^songs/$',
        ListView.as_view(
            queryset=Song.objects.all,
            context_object_name='song_list',
            template_name='song_list.html'),
        name='song_list'),
    url(r'^albums/$',
        ListView.as_view(
            queryset=Album.objects.all,
            context_object_name='album_list',
            template_name='album_list.html'),
        name='album_list'),
    url(r'^playlists/$',
        ListView.as_view(
            queryset=Playlist.objects.all,
            context_object_name='playlist_list',
            template_name='playlist_list.html'),
        name='playlist_list'),
]

urlpatterns += [
    # url(r'^login', views.login, name="login")
    # urlpatterns += [
    # RESTful API
    url(r'^api/artist/$',
        APIArtistList.as_view(), name='artist-list'),
    url(r'^api/artist/(?P<pk>\d+)/$',
        APIArtistDetail.as_view(), name='artist-detail'),
    url(r'^api/playlist/$',
        login_required(APIPlaylistList.as_view()), name='playlist-list'),
    url(r'^api/playlist/(?P<pk>\d+)/$',
        APIPlaylistDetail.as_view(), name='playlist-detail'),
    url(r'^api/song/$',
        APISongList.as_view(), name='song-list'),
    url(r'^api/song/(?P<pk>\d+)/$',
        APISongDetail.as_view(), name='song-detail'),
    url(r'^api/album/$',
        APIAlbumList.as_view(), name='album-list'),
    url(r'^api/song/(?P<pk>\d+)/$',
        APIAlbumDetail.as_view(), name='album-detail'),
    # ]
]


urlpatterns = format_suffix_patterns(urlpatterns, allowed=[
'api', 'json', 'xml'])
