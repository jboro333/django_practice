# from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth.models import User


class Artista(models.Model):
    id_artista = models.AutoField(primary_key=True)
    name_artista = models.TextField(max_length=50)
    # user = models.ForeignKey(User)

    def __unicode__(self):
            return self.name_artista

    def __str__(self):  # python 3
        return self.name_artista


class Album(models.Model):
    id_album = models.AutoField(primary_key=True)
    name_album = models.TextField(max_length=50)
    artista = models.ForeignKey(Artista)

    def __unicode__(self):
            return self.name_album

    def __str__(self):  # python 3
        return self.name_album


class Song(models.Model):
    id_song = models.AutoField(primary_key=True)
    name_song = models.TextField(max_length=50)
    artista = models.ForeignKey(Artista)
    album = models.ForeignKey(Album)

    def __unicode__(self):
            return self.name_song

    def __str__(self):  # python 3
        return self.name_song


class Playlist(models.Model):
    id_playlist = models.AutoField(primary_key=True)
    name_playlist = models.TextField(max_length=50)
    # playlist = models.ForeignKey(Song)

    def __unicode__(self):
            return self.name_playlist

    def __str__(self):  # python 3
        return self.name_playlist
