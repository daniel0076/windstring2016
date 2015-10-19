# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20151013_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='contact',
            field=models.CharField(verbose_name='聯絡人姓名', default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='player1',
            field=models.CharField(verbose_name='隊員1', help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲', max_length=50),
        ),
        migrations.AlterField(
            model_name='group',
            name='player2',
            field=models.CharField(verbose_name='隊員2', help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲', blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='group',
            name='player3',
            field=models.CharField(verbose_name='隊員3', help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲', blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='group',
            name='player4',
            field=models.CharField(verbose_name='隊員4', help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲', blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='group',
            name='player5',
            field=models.CharField(verbose_name='隊員5', help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲', blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='group',
            name='player6',
            field=models.CharField(verbose_name='隊員6', help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲', blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='group',
            name='player7',
            field=models.CharField(verbose_name='隊員7', help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲', blank=True, max_length=50),
        ),
    ]
