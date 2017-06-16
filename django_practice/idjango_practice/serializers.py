from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework.relations import HyperlinkedIdentityField, HyperlinkedRelatedField, SlugRelatedField
from models import Artist, Song, Playlist, Album, Review, ArtistReview


# es la unica API que funciona
class ArtistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='idjango_practice:api-artist-detail')

    class Meta:
        model = Artist
        fields = ('id_artist', 'name_artist', 'uri')


class SongSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='idjango_practice:api-song-detail')
    artist = SlugRelatedField(many=False, read_only=True, slug_field='name_artist')
    album = SlugRelatedField(many=False, read_only=True, slug_field='name_album')

    class Meta:
        model = Song
        fields = ('id_song', 'name_song', 'artist', 'album', 'uri')  # 'artist', 'album',


class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='idjango_practice:api-album-detail')
    artist = SlugRelatedField(many=False, read_only=True, slug_field='name_artist')

    class Meta:
        model = Album
        fields = ('id_album', 'name_album', 'artist', 'uri')  # , 'artist'


class PlaylistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='idjango_practice:api-playlist-detail')

    class Meta:
        model = Playlist
        fields = ('id_playlist', 'name_playlist', 'uri')


class ArtistReviewSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='idjango_practice:api-artist-review-detail')

    class Meta:
        model = ArtistReview
        fields = ('rating', 'comment')
