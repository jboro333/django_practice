# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import idjango_practice.models


class Migration(migrations.Migration):

    dependencies = [
        ('idjango_practice', '0003_auto_20170421_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.ForeignKey(on_delete=idjango_practice.models.Artista, to='idjango_practice.Album'),
        ),
    ]
