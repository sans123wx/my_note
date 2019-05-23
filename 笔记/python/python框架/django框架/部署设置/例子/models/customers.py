from django.db import models
from django.contrib.auth.models import Group

#售后单位
class Customer(models.Model):
    title = models.CharField(max_length = 30 ,verbose_name = '售后')
    group = models.ForeignKey(Group , on_delete = models.DO_NOTHING , verbose_name = '部门')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '售后单位'
        verbose_name_plural = '售后单位'