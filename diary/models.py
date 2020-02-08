import re
from accounts.models import CustomUser
from django.db import models



class Diary(models.Model):

    user = models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.PROTECT)
    title = models.TextField(verbose_name='タイトル')
    schedule = models.DateTimeField(verbose_name='予定日', null=True)
    restaurant = models.CharField(verbose_name='店名', null=True, max_length=100)
    number = models.IntegerField(verbose_name='参加人数', default=0)
    want = models.IntegerField(verbose_name='行きたい', null=True, default=0)
    wanttext = models.TextField(verbose_name='行きたい人達', null=True, default=',')
    station = models.CharField(verbose_name='最寄り駅', blank=True, null=True, max_length=20)
    photo1 = models.ImageField(verbose_name='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name='写真3', blank=True, null=True)
    lat = models.DecimalField(verbose_name='緯度', max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(verbose_name='経度', max_digits=9, decimal_places=6, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)

    class Meta:
        verbose_name_plural = 'Diary'

    @property
    def wantlist(self):
        wantlist = self.wanttext
        wantlist = wantlist.split(",")
        r = re.compile('^[0-9]+$')
        wantlist = [s for s in wantlist if r.match(s)]
        wantlist = [CustomUser.objects.get(pk=int(i)) for i in wantlist]
        wantlist = [i.username for i in wantlist]
        wantlist = ', '.join(wantlist)
        return wantlist

    def __str__(self):
        return self.title
