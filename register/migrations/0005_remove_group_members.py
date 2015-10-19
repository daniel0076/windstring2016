# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20151005_1801'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='members',
        ),
    ]
