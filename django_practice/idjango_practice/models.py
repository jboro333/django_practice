from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class OwnUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # USERNAME_FIELD = models.CharField
    is_artist = models.BooleanField(default=False)


class Artist(models.Model):
    id_artist = models.AutoField(primary_key=True)
    name_artist = models.TextField(max_length=50)
    url = models.URLField(default="/")
    # user = models.ForeignKey(User, default=-1)
    user = models.ForeignKey(User, default=1)
    # albums = models.ForeignKey(Album)

    def __unicode__(self):
        return self.name_artist

    def __str__(self):  # python 3
        return self.name_artist

    def averageRating(self):
        reviewCount = self.artistreview_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.aristreview_set.all()])
            return ratingSum / reviewCount


class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)

    class Meta:
        abstract = True


class ArtistReview(Review):
    artist = models.ForeignKey(Artist)

    class Meta:
        unique_together = ("artist", "user")


class Album(models.Model):
    id_album = models.AutoField(primary_key=True, default=-1)
    name_album = models.TextField(max_length=50)
    artist = models.ForeignKey(Artist, default=-1)

    def __unicode__(self):
        return self.name_album

    def __str__(self):  # python 3
        return self.name_album

    def get_absolute_url(self):
        return reverse('TuMusica:album-detail', kwargs={'pk': self.pk})


class Song(models.Model):
    id_song = models.AutoField(primary_key=True, default=-1)
    name_song = models.TextField(max_length=50)
    artist = models.ForeignKey(Artist, default=-1)
    album = models.ForeignKey(Album, default=-1)

    def __str__(self):  # python 3
        return self.name_song
    """
    def __unicode__(self):
            return self.name_song

    def get_absolute_url(self):
        return reverse('TuMusica:song-detail', kwargs={'pk': self.pk})
    """


class Playlist(models.Model):
    id_playlist = models.AutoField(primary_key=True, default=1)
    name_playlist = models.TextField(max_length=50)
    user = models.ForeignKey(User)
    songs = models.ManyToManyField(Song)

    def __unicode__(self):
            return self.name_playlist

    def __str__(self):  # python 3
        return self.name_playlist

    def get_absolute_url(self):
        return reverse('TuMusica:playlist-detail', kwargs={'pk': self.pk})
