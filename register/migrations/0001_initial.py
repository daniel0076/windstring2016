# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import register.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('gid', models.IntegerField(primary_key=True, serialize=False)),
                ('group_name', models.CharField(blank=True, verbose_name='團名', max_length=30)),
                ('song', models.CharField(max_length=30, verbose_name='預賽歌曲名')),
                ('final_song', models.CharField(blank=True, verbose_name='決賽歌曲名', max_length=30)),
                ('category', models.CharField(max_length=3, verbose_name='類別', choices=[('個人組', '個人組'), ('演奏組', '演奏組'), ('團體組', '團體組')])),
                ('leader_name', models.CharField(max_length=5, verbose_name='隊長姓名')),
                ('leader_phone', models.CharField(validators=[register.models.validate_mobile], max_length=10, verbose_name='隊長電話', help_text='格式: 0912-345678')),
                ('leader_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('members', models.TextField(verbose_name='隊員名單')),
                ('total', models.SmallIntegerField(verbose_name='參賽人數')),
                ('youtube_id', models.CharField(blank=True, verbose_name='Youtube連結', max_length=20)),
                ('votes', models.IntegerField(blank=True, verbose_name='票數')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('pay_token', models.CharField(max_length=64, verbose_name='繳費序號')),
                ('notified', models.BooleanField(verbose_name='已通知', default=False)),
                ('paid', models.BooleanField(verbose_name='已付款', default=False)),
                ('gid', models.OneToOneField(to='register.Group', db_column='group_id')),
            ],
        ),
    ]
