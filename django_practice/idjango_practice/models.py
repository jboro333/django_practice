from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Artist(models.Model):
    id_artist = models.IntegerField()
    name = models.TextField()

    def getArtistInfo(slef):
        pass


class Song(models.Model):
    id_song = models.IntegerField()
    name_song = models.TextField()

    def getSongInfo(slef):
        pass


class Album(models.Model):
    id_album = models.IntegerField()
    name_album = models.TextField()

    def getAlbumInfo(slef):
        pass


class User(models.Model):
    id_user = models.IntegerField()
    name_user = models.TextField()

    def getAlbumInfo(slef):
        pass
