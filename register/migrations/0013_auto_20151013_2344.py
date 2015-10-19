# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_auto_20151013_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='pay_status',
            field=models.SmallIntegerField(choices=[(0, 0), (1, 1), (2, 2)], default=0, verbose_name='繳費狀態'),
        ),
    ]
