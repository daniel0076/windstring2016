# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_auto_20151013_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='last5',
            field=models.CharField(verbose_name='匯款末五碼', blank=True, max_length=5),
        ),
    ]
