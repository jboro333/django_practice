# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('idjango_practice', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artistuser',
            name='name',
        ),
        migrations.RemoveField(
            model_name='normaluser',
            name='name',
        ),
    ]
