# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Student(models.Model):
    sname = models.CharField(max_length=30, unique=True)
    spwd = models.CharField(max_length=30)

    # class Meta:
    #     db_table = 't_stu'
    def __unicode__(self):
        return u'Student:%s'%self.sname





