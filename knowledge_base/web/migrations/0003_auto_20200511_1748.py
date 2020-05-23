# Generated by Django 2.2 on 2020-05-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20200430_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bingjixibie',
            name='bingjixibie',
            field=models.CharField(max_length=255, verbose_name='病机系别'),
        ),
        migrations.AlterField(
            model_name='bingzheng',
            name='bingji_zhifa',
            field=models.CharField(max_length=5000, verbose_name='病机-治法'),
        ),
        migrations.AlterField(
            model_name='bingzheng',
            name='binglifenxi',
            field=models.TextField(verbose_name='病理分析'),
        ),
        migrations.AlterField(
            model_name='bingzheng',
            name='lifazufang',
            field=models.TextField(verbose_name='立法组方'),
        ),
        migrations.AlterField(
            model_name='bingzheng',
            name='shiyingzhenghou',
            field=models.TextField(verbose_name='适应证候'),
        ),
        migrations.AlterField(
            model_name='lifang',
            name='bingji',
            field=models.TextField(verbose_name='病机'),
        ),
        migrations.AlterField(
            model_name='lifang',
            name='bingji_zhifa',
            field=models.CharField(max_length=255, verbose_name='病机-治法'),
        ),
        migrations.AlterField(
            model_name='lifang',
            name='lifangming',
            field=models.CharField(max_length=255, verbose_name='例方名'),
        ),
        migrations.AlterField(
            model_name='lifang',
            name='zhengxi',
            field=models.TextField(verbose_name='证析'),
        ),
        migrations.AlterField(
            model_name='lifang',
            name='zhifa',
            field=models.TextField(verbose_name='治法'),
        ),
        migrations.AlterField(
            model_name='lifang',
            name='zhuzhi',
            field=models.TextField(verbose_name='主治'),
        ),
        migrations.AlterField(
            model_name='zhibingjili',
            name='bingji_zhifa',
            field=models.CharField(max_length=255, verbose_name='病机-治法'),
        ),
        migrations.AlterField(
            model_name='zhibingjili',
            name='bingjixibie',
            field=models.CharField(max_length=255, verbose_name='病机系别'),
        ),
        migrations.AlterField(
            model_name='zhibingjili',
            name='zhifaleibie',
            field=models.CharField(max_length=255, verbose_name='治法类别'),
        ),
    ]