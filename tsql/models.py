from django.db import models

# Create your models here.


class Record(models.Model):
    pass_date = models.DateTimeField(verbose_name='通过时间', auto_now_add=True)
    img_path = models.CharField(verbose_name='采集图像', max_length=255)
    user_id = models.IntegerField(verbose_name='通过人员', blank=True, null=True)

    class Meta:
        db_table = 'record'
        verbose_name = '通过记录'
        verbose_name_plural = '通过记录'