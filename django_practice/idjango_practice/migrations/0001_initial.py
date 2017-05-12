# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id_album', models.AutoField(serialize=False, primary_key=True)),
                ('name_album', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ArtistUser',
            fields=[
                ('id_artista', models.AutoField(serialize=False, primary_key=True)),
                ('is_artist', models.BooleanField(default=True)),
                ('name', models.TextField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('id_user', models.AutoField(serialize=False, primary_key=True)),
                ('is_artist', models.BooleanField(default=False)),
                ('name', models.TextField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id_playlist', models.AutoField(serialize=False, primary_key=True)),
                ('name_playlist', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id_song', models.AutoField(serialize=False, primary_key=True)),
                ('name_song', models.TextField(max_length=50)),
                ('album', models.ForeignKey(to='idjango_practice.Album')),
                ('artist', models.ForeignKey(default=-1, to='idjango_practice.ArtistUser')),
            ],
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(to='idjango_practice.Song'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(default=-1, to='idjango_practice.NormalUser'),
        ),
        migrations.AddField(
            model_name='album',
            name='artista',
            field=models.ForeignKey(to='idjango_practice.ArtistUser'),
        ),
    ]
