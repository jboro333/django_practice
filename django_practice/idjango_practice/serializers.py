from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField
from models import Artist, Song, Playlist, Album


# es la unica API que funciona
class ArtistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='api-artist-detail')

    class Meta:
        model = Artist

        fields = ('uri','name_artist')


#class Meta:
#    model = Artist
#    fields = ('uri', 'song', 'playlist_set', 'user', 'name_artist', 'album')


class AlbumSerializer(HyperlinkedModelSerializer):
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

        fields = ('artist', 'name_album')

        fields = ('url', 'artist')

        fields = ('uri', 'id_artist', 'name_artist')


class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='api-album-detail')
    # artist = HyperlinkedRelatedField(view_name='artist_detail', read_only=True)

    class Meta:
        model = Album
        fields = ('uri', 'artist', 'name_album')


class SongSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='api-song-detail')
    album = HyperlinkedRelatedField(read_only=True, view_name='album-detail')
    artist = HyperlinkedRelatedField(read_only=True, view_name='artist-detail')

    class Meta:
        model = Song

        fields = ('uri', 'name_song', 'artist', 'album')

class PlaylistSerializer(HyperlinkedModelSerializer):

        fields = ('uri', 'name_song', 'artist', 'album')

class PlaylistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='api-playlist-detail')
    songs = HyperlinkedRelatedField(view_name='song_detail', read_only=True)

    class Meta:
        model = Playlist


        fields = ('url', 'name_playlist', 'songs')

        fields = ('url', 'name_playlist')

        fields = ('uri', 'name_playlist', 'songs', 'user')
