# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='votes',
        ),
        migrations.RemoveField(
            model_name='group',
            name='youtube_id',
        ),
        migrations.AlterField(
            model_name='group',
            name='category',
            field=models.CharField(verbose_name='參賽組別', max_length=3, choices=[('個人組', '個人組'), ('演奏組', '演奏組'), ('團體組', '團體組')]),
        ),
        migrations.AlterField(
            model_name='group',
            name='leader_email',
            field=models.EmailField(verbose_name='聯絡Email', max_length=254),
        ),
        migrations.AlterField(
            model_name='group',
            name='leader_name',
            field=models.CharField(verbose_name='聯絡人姓名', max_length=5),
        ),
        migrations.AlterField(
            model_name='group',
            name='leader_phone',
            field=models.CharField(verbose_name='聯絡人電話', help_text='格式: 0912-345678', max_length=10, validators=[register.models.validate_mobile]),
        ),
    ]
