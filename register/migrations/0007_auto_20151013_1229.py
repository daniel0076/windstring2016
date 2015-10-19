# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_auto_20151012_2142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='gid',
        ),
        migrations.AddField(
            model_name='group',
            name='pay_status',
            field=models.SmallIntegerField(choices=[(0, '未繳費'), (1, '已通知付款'), (2, '已繳費')], verbose_name='繳費狀態', max_length=3, default=0),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
