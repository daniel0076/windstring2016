# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_remove_group_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='ps',
            field=models.CharField(max_length=100, verbose_name='備註', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='email',
            field=models.EmailField(help_text='繳費、相關資訊會寄給您', max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='group',
            name='fb_url',
            field=models.CharField(help_text='聯絡人FB', max_length=50, verbose_name='Facebook 連結'),
        ),
        migrations.AlterField(
            model_name='group',
            name='player1',
            field=models.CharField(help_text='例：交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', max_length=50, verbose_name='隊員1'),
        ),
        migrations.AlterField(
            model_name='group',
            name='player2',
            field=models.CharField(help_text='例：交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', max_length=50, verbose_name='隊員2', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='player3',
            field=models.CharField(help_text='例：交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', max_length=50, verbose_name='隊員3', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='player4',
            field=models.CharField(help_text='例：交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', max_length=50, verbose_name='隊員4', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='player5',
            field=models.CharField(help_text='例：交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', max_length=50, verbose_name='隊員5', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='player6',
            field=models.CharField(help_text='例：交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', max_length=50, verbose_name='隊員6', blank=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='player7',
            field=models.CharField(help_text='例：交通大學 外文系 二年級 湯瑪斯-吉他手+和聲', max_length=50, verbose_name='隊員7', blank=True),
        ),
    ]
