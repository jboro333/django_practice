# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-26 20:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('idjango_practice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='id',
        ),
        migrations.RemoveField(
            model_name='artist',
            name='id',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='id',
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='song',
            name='id',
        ),
        migrations.AddField(
            model_name='album',
            name='id_album',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='artist',
            name='id_artist',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='artist',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='playlist',
            name='id_playlist',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='song',
            name='id_song',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='idjango_practice.Artist'),
        ),
    ]
