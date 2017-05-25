from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class OwnUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #USERNAME_FIELD = models.CharField
    is_artist = models.BooleanField(default=False)


class Artist(models.Model):
    id_artist = models.AutoField(primary_key=True)
    name_artist = models.TextField(max_length=50)
    # albums = models.ManyToManyField(Album)

    def __unicode__(self):
            return self.name_artist

    def __str__(self):  # python 3
        return self.name_artist


class Album(models.Model):
    id_album = models.AutoField(primary_key=True)
    name_album = models.TextField(max_length=50)
    artist = models.ForeignKey(Artist, default=-1)

    def __unicode__(self):
            return self.name_album

    def __str__(self):  # python 3
        return self.name_album


class Song(models.Model):
    id_song = models.AutoField(primary_key=True)
    name_song = models.TextField(max_length=50)
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)

    def __unicode__(self):
            return self.name_song

    def __str__(self):  # python 3
        return self.name_song


class Playlist(models.Model):
    id_playlist = models.AutoField(primary_key=True)
    name_playlist = models.TextField(max_length=50)
    user = models.ForeignKey(User)
    songs = models.ManyToManyField(Song)

    def __unicode__(self):
            return self.name_playlist

    def __str__(self):  # python 3
        return self.name_playlist
