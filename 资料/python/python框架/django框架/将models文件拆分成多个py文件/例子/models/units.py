from django.db import models
from .customers import *

#设备类型
class Unit_type(models.Model):
    title = models.CharField(max_length = 30 , verbose_name = '类型')
    sh = models.ForeignKey(Customer,on_delete = models.DO_NOTHING ,
                           verbose_name = '售后单位')
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '设备类型'
        verbose_name_plural = '设备类型'

#设备型号
class Unit_model(models.Model):
    lx  = models.ForeignKey(Unit_type , on_delete = models.DO_NOTHING ,
                             verbose_name = '类型')
    title = models.CharField(max_length = 30 , verbose_name = '型号')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '设备型号'
        verbose_name_plural = '设备型号'