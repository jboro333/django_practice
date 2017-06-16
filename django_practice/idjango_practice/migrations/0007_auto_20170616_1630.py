# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idjango_practice', '0006_auto_20170616_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='id_playlist',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(to='idjango_practice.Album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(to='idjango_practice.Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='id_song',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
