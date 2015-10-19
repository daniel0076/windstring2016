# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20151004_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='leader_email',
            field=models.EmailField(verbose_name='Email', max_length=254),
        ),
        migrations.AlterField(
            model_name='group',
            name='leader_name',
            field=models.CharField(verbose_name='姓名', max_length=5),
        ),
        migrations.AlterField(
            model_name='group',
            name='leader_phone',
            field=models.CharField(max_length=11, verbose_name='電話', validators=[register.models.validate_mobile], help_text='格式: 0912-345678'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='gid',
            field=models.ForeignKey(db_column='group_id', to='register.Group'),
        ),
    ]
