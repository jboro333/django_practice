# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idjango_practice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.ForeignKey(default=-1, to='idjango_practice.Artist'),
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(default=-1, to='idjango_practice.Album'),
        ),
        migrations.AlterField(
            model_name='song',
            name='id_song',
            field=models.AutoField(default=-1, serialize=False, primary_key=True),
        ),
    ]
