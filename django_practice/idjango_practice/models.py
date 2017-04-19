
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Artist(models.Model):
    id_artist = models.IntegerField(balnk=False, null=False)
    name = models.TextField()
    albums = models.ForeignKey(Album, null=False, blank=False)
    url = models.URLField()
    user = models.ForeignKey(User, default=1)

    def getArtistInfo(slef):
        pass

    def getAlbums(self):
        pass


class Song(models.Model):
    id_song = models.IntegerField()
    name_song = models.TextField()
    album = models.ForeignKey(Album, null=False)
    url = models.URLField()

    def getSongInfo(slef):
        pass


class Album(models.Model):
    id_album = models.IntegerField(blank=False, null=False)
    name_album = models.TextField()
    url = models.URLField()

    def getAlbumInfo(slef):
        pass


class User(models.Model):
    id_user = models.IntegerField()
    name_user = models.TextField()

    def getAlbumInfo(slef):
        pass
