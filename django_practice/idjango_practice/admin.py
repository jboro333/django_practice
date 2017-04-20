from django.contrib import admin
# import models
from idjango_practice.models import Artist, Song, Album, User, PlayList

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(PlayList)
# Register your models here.
