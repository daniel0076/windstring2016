# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20151013_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='others',
        ),
        migrations.AlterField(
            model_name='group',
            name='fb_url',
            field=models.CharField(help_text='聯絡人FB', max_length=100, verbose_name='Facebook 連結'),
        ),
    ]
