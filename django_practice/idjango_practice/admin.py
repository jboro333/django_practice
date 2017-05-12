from django.contrib import admin
from .models import Album, ArtistUser, NormalUser, Song, Playlist

admin.site.register(Album)
admin.site.register(ArtistUser)
admin.site.register(NormalUser)
admin.site.register(Song)
admin.site.register(Playlist)
