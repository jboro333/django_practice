# from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Album(models.Model):
    id_album = models.IntegerField(blank=False, null=False)
    name_album = models.TextField()
    url = models.URLField()

    def getAlbumInfo(self):
        pass


class Artist(models.Model):
    id_artist = models.IntegerField(blank=False, null=False)
    name = models.TextField()
    albums = models.ForeignKey(Album, blank=False, null=False)
    url = models.URLField()

    def getArtistInfo(self):
        pass


class Song(models.Model):
    id_song = models.IntegerField()
    name_song = models.TextField()
    album = models.ForeignKey(Album, null=False)
    url = models.URLField()

    def getSongInfo(self):
        pass
