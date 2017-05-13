from django.contrib import admin
from .models import Album, Artist, Song, Playlist
# from django.contrib.auth.admin import UserAdmin, BaseUserAdmin
# from django.contrib.auth.models import User

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Playlist)
