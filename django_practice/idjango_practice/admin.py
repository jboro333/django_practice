from django.contrib import admin

from idjango_practice.models import Artist, Song, Album, User

admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Album)
admin.site.register(User)
# Register your models here.
