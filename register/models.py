from __future__ import unicode_literals
from django.db import models
from django.core.validators import RegexValidator,MinLengthValidator,validate_email
from django.utils import timezone
# Create your models here.

def validate_mobile(string):
    RegexValidator(regex='^\d{10}$',message='格式：0987654321')(string)

class Group(models.Model):
    CATEGORYS = (
            (u'個人組', u'個人組'),
            (u'演奏組', u'演奏組'),
            (u'團體組', u'團體組')
            )
    STATUS = (
            (0, 0),
            (1, 1),
            (2, 2)
            )
    gid = models.IntegerField(primary_key=True)  # AutoField
    group_name= models.CharField(u'團名',max_length=30,blank=True)
    category = models.CharField(u'參賽組別',max_length=3,choices=CATEGORYS,default=u'個人組')
    song = models.CharField(u'預賽歌曲名',max_length=30)
    final_song = models.CharField(u'決賽歌曲名',max_length=30,blank=True)
    cellphone= models.CharField(u'手機號碼',max_length=10,validators=[validate_mobile],help_text='聯絡人手機（團體組請用一個代表）')
    email= models.EmailField(u'Email',help_text='繳費、相關資訊會寄給您')
    contact= models.CharField(u'聯絡人姓名',max_length=50)
    fb_url= models.CharField(u'Facebook 連結',max_length=100,help_text='聯絡人FB')
    player1=models.CharField(u'隊員1',max_length=50,help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲')
    player2=models.CharField(u'隊員2',max_length=50,help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲',blank=True)
    player3=models.CharField(u'隊員3',max_length=50,help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲',blank=True)
    player4=models.CharField(u'隊員4',max_length=50,help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲',blank=True)
    player5=models.CharField(u'隊員5',max_length=50,help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲',blank=True)
    player6=models.CharField(u'隊員6',max_length=50,help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲',blank=True)
    player7=models.CharField(u'隊員7',max_length=50,help_text='例：交通大學 材料系 二年級 蝦哥哥-吉他手+和聲',blank=True)
    mic=models.SmallIntegerField('麥克風',blank=True,default=0)
    mic_holder=models.SmallIntegerField('麥克風架',blank=True,default=0)
    chair=models.SmallIntegerField('椅子',blank=True,default=0)
    ps=models.CharField(u'備註',max_length=100,blank=True,default="無")
    pay_status= models.SmallIntegerField(u'繳費狀態',choices=STATUS,default=0)
    last5=models.CharField(u'匯款末五碼',max_length=5,blank=True)
