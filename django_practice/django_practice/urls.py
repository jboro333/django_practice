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

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from idjango_practice import views
from django.views.generic import ListView  # DetailView, UpdateView
from rest_framework.urlpatterns import format_suffix_patterns
from idjango_practice.forms import *
from idjango_practice.models import Playlist, Artist, Song, Album
from idjango_practice.serializers import *
from idjango_practice.views import review

urlpatterns = [
    # url de la pagina principal
    url(r'^$', views.home, name="home"),
    url(r'^home', views.home, name="home"),
    # url login, logout y contacto
    url(r'^login/$', views.Login),
    url(r'^logout/$', views.Logout),
    url(r'^contact', views.contact, name="contact"),
    # url del panle de administracion
    url(r'^admin/', admin.site.urls),
    # url's de los formularios de creacion
    url(r'^artist/create/$', views.ArtistCreate.as_view(), name='artist_create'),
    url(r'^song/create', views.SongCreate.as_view(), name="song_create"),
    url(r'^album/create$', views.AlbumCreate.as_view(), name="album_create"),
    url(r'^playlist/create', views.PlaylistCreate.as_view(), name="playlist_create"),
    # urls's de detalles de los objetos
    url(r'^artist/(?P<pk>\d+)/$', views.ArtistDetail.as_view(),
        name='artist_detail'),
    url(r'^song/(?P<pk>\d+)/$', views.SongDetail.as_view(), name="song_detail"),
    url(r'^album/(?P<pk>\d+)/$', views.AlbumDetail.as_view(), name="album_detail"),
    url(r'^playlist/(?P<pk>\d+)/$', views.PlaylistDetail.as_view(), name="playlist_detail"),

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

    # Create a artist review
    url(r'^artists/(?P<pk>\d+)/reviews/create/$',
        review,
        name='review_create'),
]

urlpatterns += [
    url(r'^api/artist/$',
        views.APIArtistList.as_view(), name='api-artist-list'),
    url(r'^api/artist/(?P<pk>\d+)/$',
        views.APIArtistDetail.as_view(), name='api-artist-detail'),
    url(r'^api/playlist/$',
        views.APIPlaylistList.as_view(), name='api-playlist-list'),
    url(r'^api/playlist/(?P<pk>\d+)/$',
        views.APIPlaylistDetail.as_view(), name='api-playlist-detail'),
    url(r'^api/song/$',
        views.APISongList.as_view(), name='api-song-list'),
    url(r'^api/song/(?P<pk>\d+)/$',
        views.APISongDetail.as_view(), name='api-song-detail'),
    url(r'^api/album/$',
        views.APIAlbumList.as_view(), name='api-album-list'),
    url(r'^api/album/(?P<pk>\d+)/$',
        views.APIAlbumDetail.as_view(), name='api-album-detail'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api', 'json', 'xml'])

"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
"""
