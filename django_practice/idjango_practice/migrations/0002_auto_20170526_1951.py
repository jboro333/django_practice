# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idjango_practice', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='id_artist',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
