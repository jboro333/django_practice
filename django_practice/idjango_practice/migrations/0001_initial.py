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
                ('id_album', models.AutoField(default=-1, serialize=False, primary_key=True)),
                ('name_album', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id_artist', models.AutoField(serialize=False, primary_key=True)),
                ('name_artist', models.TextField(max_length=50)),
                ('url', models.URLField(default='/')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OwnUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_artist', models.BooleanField(default=False)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id_playlist', models.AutoField(default=1, serialize=False, primary_key=True)),
                ('name_playlist', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id_song', models.AutoField(default=1, serialize=False, primary_key=True)),
                ('name_song', models.TextField(max_length=50)),
                ('album', models.ForeignKey(default=2, to='idjango_practice.Album')),
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
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default=-1, to='idjango_practice.Artist'),
        ),
    ]
