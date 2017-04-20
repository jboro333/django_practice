from django.contrib import admin
# import models
from idjango_practice.models import Album, Artist, Song, Playlist

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Playlist)
