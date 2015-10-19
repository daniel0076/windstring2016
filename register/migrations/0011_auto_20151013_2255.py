# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_group_last5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='ps',
            field=models.CharField(verbose_name='備註', blank=True, max_length=100, default='無'),
        ),
    ]
