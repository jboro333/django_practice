
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


# Create your models here.
class Artist(models.Model):
    id_artist = models.IntegerField() # (blank=False, null=False)
    artist_name = models.TextField()
    # url = models.URLField()
    # user = models.ForeignKey(User)

    def getArtistInfo(self):
        pass # return "Artist name: " + self.artist_name
	"""
    def __unicode__(self):
        return u"%s" % self.artist_name

    def getArtistUrl(self):
        pass
    """


class Album(models.Model):
    id_album = models.IntegerField()
    album_name = models.TextField()
    # artist = models.ForeignKey(Artist)
    # url = models.URLField()

    def getAlbumInfo(self):
        pass # return "Album name: " + self.album_name
    """
    def __unicode__(self):
        return u"%s" % self.album_name

    def getAlbumUrl(self):
        pass
        """


class Song(models.Model):
    id_song = models.IntegerField()
    song_name = models.TextField()
    # album = models.ForeignKey(Album)
    # artist = models.ForeignKey(Artist)
    # url = models.URLField()

    def getSongInfo(self):
        pass # return "Song name: " + self.song_name
    """
    def __unicode__(self):
        return u"%s" % self.song_name

    def getSongUrl(self):
        pass
        """


class PlayList(models.Model):
    id_playlist = models.IntegerField()
    name_playlist = models.TextField()
    # songs = models.ForeignKey(Song)
    url = models.URLField()
    # playlist = models.ForeignKey(PlayList)

    def getPlayListInfo(self):
        pass # return "Play list name: " + self.name_playlist
    """
    def __unicode__(self):
        return u"%s" % self.name_playlist

    def getPlayListUrl(self):
        pass
        """
