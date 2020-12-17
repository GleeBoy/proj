from django.db import models

# Create your models here.


class Widget(models.Model):
    name = models.CharField('名字', max_length=24)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')