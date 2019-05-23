from django.db import models
from .customers import *

#报账时间
class Report_time(models.Model):
    title = models.CharField(max_length = 30,verbose_name = '名称')
    bz = models.CharField(max_length = 30 , default = '无' , verbose_name = '备注')
    bzsj = models.DateField(verbose_name = '报账时间')
    sh = models.ForeignKey(Customer , on_delete = models.DO_NOTHING , verbose_name = '售后')
    used = models.BooleanField(default = False , verbose_name = '是否已使用')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '报账时间'
        verbose_name_plural = '报账时间'
        ordering = ['-bzsj']