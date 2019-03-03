from django.db import models
from django.contrib.auth.models import User , Group
from django.utils import timezone
from django.shortcuts import Http404
from .units import *
from .customers import *
from .report_times import *


#维修记录
class Note(models.Model):
    date = models.DateField(default = timezone.now)
    lb = models.ForeignKey(Unit_type , on_delete = models.DO_NOTHING ,
                           verbose_name = '类型')
    xh = models.ForeignKey(Unit_model , on_delete = models.DO_NOTHING ,
                            verbose_name = '型号')
    gz = models.CharField(max_length = 30 , verbose_name = '故障')
    jg = models.FloatField(verbose_name = '价格')
    sl = models.IntegerField(verbose_name = '数量')
    dd = models.CharField(max_length = 30 , verbose_name = '地点')
    bz = models.BooleanField(verbose_name = '报账')
    fs = models.CharField(max_length = 30 , verbose_name = '方式')
    sh = models.ForeignKey(Customer , on_delete = models.DO_NOTHING ,
                           verbose_name = '售后')
    zt = models.CharField(max_length = 15 , default = '未通知售后')
    tzsj = models.DateField(blank = True , null = True , verbose_name = '通知时间')
    dxsj = models.DateField(blank = True , null = True , verbose_name = '到校时间')
    fxsj = models.DateField(blank = True , null = True , verbose_name = '返校时间')
    xysc = models.DurationField(blank = True , null = True , verbose_name = '响应时长')
    xfsc = models.DurationField(blank = True , null = True , verbose_name = '修复时长')
    bzsj = models.ForeignKey(Report_time , on_delete = models.DO_NOTHING ,
                             blank = True , null = True , verbose_name = '报账时间')
    hj = models.FloatField(blank = True , null = True , verbose_name = '合计')
    owner = models.ForeignKey(User , on_delete = models.DO_NOTHING , verbose_name = '创建者')
    sn = models.CharField(max_length = 30,blank = True , null = True , default = '无' ,
                          verbose_name = '序列号')
    shry = models.CharField(max_length = 30,blank = True , null = True ,
                            verbose_name = '售后人员')
    shdh = models.CharField(max_length = 30,blank = True , null = True ,
                            verbose_name = '电话')

    def __str__(self):
        return self.lb.title

    def save(self):
        self.hj = self.jg * self.sl
        self.状态 = '未通知售后'
        if self.tzsj:self.zt = '已通知售后'   
        if self.dxsj:
            if not self.tzsj:
                raise Http404
            else:
                self.zt = '设备已返厂'
                self.xysc = self.dxsj - self.tzsj
        if self.fxsj:
            if not self.dxsj:
                raise Http404
            elif not self.scraped:
                self.状态 = '设备已修复'
                self.sfsc = self.fxsj - self.dxsj
            else:
                self.zt = '设备报废'
        super().save()
        

    class Meta:
        ordering = ['-date']
        verbose_name = '维修记录'
        verbose_name_plural = '维修记录'

