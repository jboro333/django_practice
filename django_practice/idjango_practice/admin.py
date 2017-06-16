from django.contrib import admin
from .models import Album, Artist, Song, Playlist, ArtistReview
# from django.contrib.auth.admin import UserAdmin, BaseUserAdmin
# from django.contrib.auth.models import User
from .forms import AlbumForm, ArtistForm, SongForm, PlaylistForm


class AdminSong(admin.ModelAdmin):
    form = SongForm
    list_filter = []
    list_editable = []
    list_display = []
    search_fields = []


class AdminPlaylist(admin.ModelAdmin):
    form = PlaylistForm
    list_filter = []
    list_editable = []
    list_display = []
    search_fields = []


class AdminArtist(admin.ModelAdmin):
    form = ArtistForm
    list_filter = []
    list_editable = []
    list_display = []
    search_fields = []


class AdminAlbum(admin.ModelAdmin):
    form = AlbumForm
    list_filter = []
    list_editable = []
    list_display = []
    search_fields = []


admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Playlist)
admin.site.register(ArtistReview)
"""
admin.site.register(Album, AdminAlbum)
admin.site.register(Song, AdminSong)
admin.site.register(Artist, AdminArtist)
admin.site.register(Playlist, AdminPlaylist)
"""
