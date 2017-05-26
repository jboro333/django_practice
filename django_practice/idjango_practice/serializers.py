from rest_framework import serializers
from models import *
#from models import Artist, Album, Song, Playlist


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    # uri = HyperlinkedIdentityField(view_name='TuMusica:artist-detail')
    # album = HyperlinkedRelatedField(
    #    many=True, read_only=True,
    #    view_name='TuMusica:album-detail')
    # song = HyperlinkedRelatedField(
    #    many=True, read_only=True,
    #    view_name='TuMusica_song-detail')
    # playlist_set = HyperlinkedRelatedField(
    #    many=True, read_only=True,
    #    view_name='TuMusica:playlist-detail')
    # user = CharField(read_only=True)

    class Meta:
        model = Artist
        fields = ('url', 'name_artist')


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    #uri = HyperlinkedIdentityField(view_name='TuMusica:album-detail')
    #artist = HyperlinkedRelatedField(view_name='TuMusica:artist-detail', read_only=True)
    #songs = HyperlinkedRelatedField(many=True, read_only=True, view_name='TuMusica_song-detail')
    #artist = HyperlinkedRelatedField(
    #    view_name='TuMusica:artist-detail', read_only=True)
    #songs = HyperlinkedRelatedField(
    #    many=True, read_only=True, view_name='TuMusica_song-detail')
    #user = CharField(read_only=True)

    class Meta:
        model = Album
        fields = ('url', 'artist')


class SongSerializer(serializers.HyperlinkedModelSerializer):
    #uri = HyperlinkedIdentityField(view_name='TuMusica:song-detail')
    #artist = HyperlinkedRelatedField(
    #    view_name='TuMusica:artist-detail', read_only=True)
    #album = HyperlinkedRelatedField(
    #    many=True, read_only=True, view_name='TuMusica:album-detail')
    #user = CharField(read_only=True)

    class Meta:
        model = Song
        fields = ('url', 'name_song', 'artist', 'album')


class PlaylistSerializer(serializers.HyperlinkedModelSerializer):

    #uri = HyperlinkedIdentityField(view_name='TuMusica:playlist-detail')
    #song = HyperlinkedRelatedField(view_name='TuMusica:song-detail', read_only=True)
    #song = HyperlinkedRelatedField(
    #    view_name='TuMusica:song-detail', read_only=True)
    #user = CharField(read_only=True)

    class Meta:
        model = Playlist
        fields = ('url', 'name_playlist')
