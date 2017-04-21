# from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User


class Artista(models.Model):
    id_artista = models.IntegerField(default=0)
    name_artista = models.TextField(max_length=50)
    artista = models.ForeignKey(User)

    def __unicode__(self):
            return self.id_artista


class Album(models.Model):
    id_album = models.IntegerField()
    name_album = models.TextField(max_length=50)
    album = models.ForeignKey(Artista)

    def __unicode__(self):
            return self.id_album


class Song(models.Model):
    id_song = models.IntegerField()
    name_song = models.TextField()
    song = models.ForeignKey(Album, Artista)

    def __unicode__(self):
            return self.id_song


class Playlist(models.Model):
    id_playlist = models.IntegerField()
    name_playlist = models.TextField(max_length=50)
    playlist = models.ForeignKey(Song)

    def __unicode__(self):
            return self.id_playlist
