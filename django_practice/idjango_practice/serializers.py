from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField, SlugRelatedField
from models import Artist, Song, Playlist, Album


# es la unica API que funciona
class ArtistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='api-artist-detail')

    class Meta:
        model = Artist

        fields = ('uri', 'name_artist')


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
        model = Album
        fields = ('id_album', 'artist')


class PlaylistSerializer(HyperlinkedModelSerializer):
    # uri = HyperlinkedIdentityField(view_name='api-playlist-detail')
    # list_songs = SlugRelatedField(many=True, slug_field='name_song', read_only=True)

    class Meta:
        model = Playlist
        fields = ('id_playlist', 'name_playlist', 'songs')
