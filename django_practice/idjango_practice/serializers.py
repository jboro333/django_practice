
from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from models import *

class ArtistSerializer(HyperlinkedModelSerializer):

 uri = HyperlinkedIdentityField(view_name='TuMusica:artist-detail')
 album = HyperlinkedRelatedField(many=True, read_only=True, view_name='TuMusica:album-detail')
 song = HyperlinkedRelatedField(many=True, read_only=True,view_name='TuMusica_song-detail')
 playlist_set = HyperlinkedRelatedField(many=True, read_only=True,view_name='TuMusica:playlist-detail')
 user = CharField(read_only=True)

 class Meta:
     model = Artist
     fields = ('uri', 'id_artist','name_artist','albums', 'songs')

class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='TuMusica:album-detail')
    artist = HyperlinkedRelatedField(view_name='TuMusica:artist-detail', read_only=True)
    songs = HyperlinkedRelatedField(many=True, read_only=True,view_name='TuMusica_song-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Album
        fields = ('uri',' name_album','artist')

class SongSerializer(HyperlinkedModelSerializer):

    uri = HyperlinkedIdentityField(view_name='TuMusica:song-detail')
    artist = HyperlinkedRelatedField(view_name='TuMusica:artist-detail', read_only=True)
    album = HyperlinkedRelatedField(many=True, read_only=True, view_name='TuMusica:album-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Song
        fields = ('uri', 'name_song','artist', 'album')

class PlaylistSerializer(HyperlinkedModelSerializer):

    uri = HyperlinkedIdentityField(view_name='TuMusica:playlist-detail')
    song = HyperlinkedRelatedField(view_name='TuMusica:song-detail', read_only=True)
    user = CharField(read_only=True)

    class Meta:
        model = Playlist
        fields = ('uri', 'name_playlist', 'user', 'song')
