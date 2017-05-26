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
"""
# urlpatterns += [
# RESTful API
#    url(r'^api/artist/$',
#        APIArtistList.as_view(), name='artist-list')],
#    url(r'^api/artist/(?P<pk>\d+)/$',
#        APIArtistDetail.as_view(), name='artist-detail'),
#    url(r'^api/playlist/$',
#        login_required(APIPlaylistList.as_view()), name='playlist-list'),
#    url(r'^api/playlist/(?P<pk>\d+)/$',
#        APIPlaylistDetail.as_view(), name='playlist-detail'),
#    url(r'^api/song/$',
#        APISongList.as_view(), name='song-list'),
#    url(r'^api/song/(?P<pk>\d+)/$',
#        APISongDetail.as_view(), name='song-detail'),
#    url(r'^api/album/$',
#        APIAlbumList.as_view(), name='album-list'),
#    url(r'^api/song/(?P<pk>\d+)/$',
#        APIAlbumDetail.as_view(), name='album-detail'),
# ]



    url(r'^$',
        ListView.as_view(
            queryset=Song.objects.filter(date__lte=timezone.now()).order_by('-d
                ate')[:5],
            context_object_name='latest_restaurant_list',
            template_name='myrestaurants/restaurant_list.html'),
        name='restaurant_list')
]



"""
