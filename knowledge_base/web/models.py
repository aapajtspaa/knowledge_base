from django.db import models


# Create your models here.


class Bingjixibie(models.Model):
    id = models.IntegerField(primary_key=True)
    bingjixibie = models.CharField(max_length=255, verbose_name='病机系别')

    def __str__(self):
        return self.bingjixibie

    class Meta:
        verbose_name_plural = verbose_name = "病机系别"


class Bingzheng(models.Model):
    id = models.IntegerField(primary_key=True)
    bingji_zhifa = models.CharField(max_length=5000, verbose_name='病机-治法')
    shiyingzhenghou = models.TextField(verbose_name='适应证候')
    binglifenxi = models.TextField(verbose_name='病理分析')
    lifazufang = models.TextField(verbose_name='立法组方')

    def __str__(self):
        return self.bingji_zhifa

    class Meta:
        verbose_name_plural = verbose_name = "病机-治法"


class Lifang(models.Model):
    id = models.IntegerField(primary_key=True)
    bingji_zhifa = models.CharField(max_length=255, verbose_name='病机-治法')
    lifangming = models.CharField(max_length=255, verbose_name='例方名')
    zhuzhi = models.TextField(verbose_name='主治')
    zhengxi = models.TextField(verbose_name='证析')
    bingji = models.TextField(verbose_name='病机')
    zhifa = models.TextField(verbose_name='治法')

    def __str__(self):
        return self.lifangming

    class Meta:
        verbose_name_plural = verbose_name = "例方"


class Zhibingjili(models.Model):
    id = models.IntegerField(primary_key=True)
    zhifaleibie = models.CharField(max_length=255, verbose_name='治法类别')
    bingji_zhifa = models.CharField(max_length=255, verbose_name='病机-治法')
    bingjixibie = models.CharField(max_length=255, verbose_name='病机系别')

    def __str__(self):
        return self.zhifaleibie

    class Meta:
        verbose_name_plural = verbose_name = "治法类别"
