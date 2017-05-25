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
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from idjango_practice import views
from idjango_practice.views import *
from django.views.generic import DetailView, ListView, UpdateView
from idjango_practice.views import *
from idjango_practice.forms import *
from idjango_practice.models import *
from idjango_practice.serializers import *
# from idjango_practice.views import Register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    # url(r'^register', views.register, name="register"),
    # url(r'^register', Register.as_view(), name='register'),
    url(r'^contact', views.contact, name="contact"),
    # url(r'^artist', ArtistDetail, name="artist"),
    # url(r'^song', views.song, name="song"),
    # url(r'^album', views.album, name="album"),
    # url(r'^playlist', views.playlist, name="playlist"),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    #url(r'^login', views.login, name="login")
#urlpatterns += [
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
    #]
]
