from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# from djangotoolbox.fields import ListField


class NormalUser(models.Model):
    id_user = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_artist = models.BooleanField(default=False)
    name = models.TextField(max_length=50)


class ArtistUser(models.Model):
    id_artista = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_artist = models.BooleanField(default=True)
    name = models.TextField(max_length=50)

    def __unicode__(self):
            return self.name

    def __str__(self):  # python 3
        return self.name


class Album(models.Model):
    id_album = models.AutoField(primary_key=True)
    name_album = models.TextField(max_length=50)
    artista = models.ForeignKey(ArtistUser)

    def __unicode__(self):
            return self.name_album

    def __str__(self):  # python 3
        return self.name_album


class Song(models.Model):
    id_song = models.AutoField(primary_key=True)
    name_song = models.TextField(max_length=50)
    artist = models.ForeignKey(ArtistUser, default=-1)
    album = models.ForeignKey(Album)

    def __unicode__(self):
            return self.name_song

    def __str__(self):  # python 3
        return self.name_song


class Playlist(models.Model):
    id_playlist = models.AutoField(primary_key=True)
    name_playlist = models.TextField(max_length=50)
    user = models.ForeignKey(NormalUser, default=-1)
    songs = models.ManyToManyField(Song)

    def __unicode__(self):
            return self.name_playlist

    def __str__(self):  # python 3
        return self.name_playlist
