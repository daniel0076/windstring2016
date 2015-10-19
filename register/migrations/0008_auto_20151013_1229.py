# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20151013_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='pay_status',
            field=models.SmallIntegerField(default=0, choices=[(0, '未繳費'), (1, '已通知付款'), (2, '已繳費')], verbose_name='繳費狀態'),
        ),
    ]
