from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField, SlugRelatedField
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


class SongSerializer(HyperlinkedModelSerializer):
    # uri = HyperlinkedIdentityField(view_name='api-song-detail')
    artist = SlugRelatedField(many=False, read_only=True, slug_field='name_artist')
    album = SlugRelatedField(many=False, read_only=True, slug_field='name_album')

    class Meta:
        model = Song
        fields = ('id_song', 'name_song', 'artist', 'album')  # , 'album')


class AlbumSerializer(HyperlinkedModelSerializer):
    # uri = HyperlinkedIdentityField(view_name='api-album-detail')
    artist = SlugRelatedField(many=False, read_only=True, slug_field='name_artist')
    # artist = HyperlinkedRelatedField(read_only=True, view_name='artist_detail')

    class Meta:
<<<<<<< HEAD
        model = Song

        fields = ('uri', 'name_song', 'artist', 'album')
=======
        model = Album
        fields = ('id_album', 'artist')
>>>>>>> c1a6d174ee9e91e8b6984f5289246363bd7e774b

class PlaylistSerializer(HyperlinkedModelSerializer):

        fields = ('uri', 'name_song', 'artist', 'album')

class PlaylistSerializer(HyperlinkedModelSerializer):
    # uri = HyperlinkedIdentityField(view_name='api-playlist-detail')
    # list_songs = SlugRelatedField(many=True, slug_field='name_song', read_only=True)

    class Meta:
        model = Playlist
<<<<<<< HEAD


        fields = ('url', 'name_playlist', 'songs')

        fields = ('url', 'name_playlist')

        fields = ('uri', 'name_playlist', 'songs', 'user')
=======
        fields = ('id_playlist', 'name_playlist', 'songs')  # 'songs', 'user'
>>>>>>> c1a6d174ee9e91e8b6984f5289246363bd7e774b
