# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20151004_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='leader_email',
        ),
        migrations.RemoveField(
            model_name='group',
            name='leader_name',
        ),
        migrations.RemoveField(
            model_name='group',
            name='leader_phone',
        ),
        migrations.RemoveField(
            model_name='group',
            name='total',
        ),
        migrations.AddField(
            model_name='group',
            name='cellphone',
            field=models.CharField(help_text='聯絡人手機（團體組請用一個代表）', default='0000-000000', verbose_name='手機號碼', max_length=11, validators=[register.models.validate_mobile]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='chair',
            field=models.SmallIntegerField(blank=True, verbose_name='椅子', default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='email',
            field=models.EmailField(help_text='連絡、通知用，之後相關資訊也會寄給您', default=0, verbose_name='Email', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='fb_url',
            field=models.CharField(help_text='聯絡人FB', default=0, verbose_name='Facebook 聯結', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='mic',
            field=models.SmallIntegerField(blank=True, verbose_name='麥克風', default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='mic_holder',
            field=models.SmallIntegerField(blank=True, verbose_name='麥克風架', default=0),
        ),
        migrations.AddField(
            model_name='group',
            name='others',
            field=models.CharField(blank=True, verbose_name='其它需求', max_length=100),
        ),
        migrations.AddField(
            model_name='group',
            name='player1',
            field=models.CharField(help_text='交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', default='g', verbose_name='樂手編制1', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='group',
            name='player2',
            field=models.CharField(help_text='交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', blank=True, verbose_name='樂手編制2', max_length=50),
        ),
        migrations.AddField(
            model_name='group',
            name='player3',
            field=models.CharField(help_text='交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', blank=True, verbose_name='樂手編制3', max_length=50),
        ),
        migrations.AddField(
            model_name='group',
            name='player4',
            field=models.CharField(help_text='交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', blank=True, verbose_name='樂手編制4', max_length=50),
        ),
        migrations.AddField(
            model_name='group',
            name='player5',
            field=models.CharField(help_text='交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', blank=True, verbose_name='樂手編制5', max_length=50),
        ),
        migrations.AddField(
            model_name='group',
            name='player6',
            field=models.CharField(help_text='交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', blank=True, verbose_name='樂手編制6', max_length=50),
        ),
        migrations.AddField(
            model_name='group',
            name='player7',
            field=models.CharField(help_text='交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', blank=True, verbose_name='樂手編制7', max_length=50),
        ),
        migrations.AlterField(
            model_name='group',
            name='category',
            field=models.CharField(default='個人組', verbose_name='參賽組別', max_length=3, choices=[('個人組', '個人組'), ('演奏組', '演奏組'), ('團體組', '團體組')]),
        ),
    ]
