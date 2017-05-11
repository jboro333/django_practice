# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
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
            name='Artista',
            fields=[
                ('id_artista', models.AutoField(serialize=False, primary_key=True)),
                ('name_artista', models.TextField(max_length=50)),
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
                ('artista', models.ForeignKey(to='idjango_practice.Artista')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='artista',
            field=models.ForeignKey(to='idjango_practice.Artista'),
        ),
    ]
