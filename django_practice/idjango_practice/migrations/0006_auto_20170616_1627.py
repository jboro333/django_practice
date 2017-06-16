# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idjango_practice', '0005_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(to='idjango_practice.Artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='id_album',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
