# from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User


class Album(models.Model):
    id_album = models.IntegerField()
    name_album = models.TextField(max_length=50)

    def __unicode__(self):
            return self.id_album


class Artist(models.Model):
    id_artist = models.IntegerField()
    name_artist = models.TextField(max_length=50)
    # artist = models.ForeignKey(User)

    def __unicode__(self):
            pass


class Song(models.Model):
    id_song = models.IntegerField()
    name_song = models.TextField()

    def __unicode__(self):
            return self.id_song


class Playlist(models.Model):
    id_playlist = models.IntegerField()
    name_playlist = models.TextField(max_length=50)

    def __unicode__(self):
            pass
