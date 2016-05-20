#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class Parametrs(models.Model):
    idparametrs = models.IntegerField(primary_key=True)
    bus_id = models.IntegerField()
    addr = models.IntegerField()
    value = models.FloatField(blank=True, null=True)
    to_log = models.IntegerField()
    addr_type = models.IntegerField()
    direction = models.IntegerField()
    description = models.CharField(max_length=45, blank=True)
    last_update = models.DateTimeField(blank=True, null=True)
    to_set = models.IntegerField()

    class Meta:
        app_label = 'celse'
        managed = True
        db_table = 'parametrs'


class Ctrls(models.Model):
    idctrls = models.IntegerField(primary_key=True)
    bus_id = models.IntegerField()
    online = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    description = models.CharField(max_length=45, blank=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'celse'
        managed = False
        db_table = 'ctrls'
        
class TCtrl(models.Model):
    idtable1 = models.IntegerField(primary_key=True)
    type_id = models.IntegerField()
    description = models.CharField(max_length=45, blank=True)

    class Meta:
        app_label = 'celse'
        managed = False
        db_table = 't_ctrl'
        
class Paramlog(models.Model):
    idparamlog = models.IntegerField(primary_key=True)
    bus_id = models.IntegerField()
    addr = models.IntegerField()
    addr_type = models.IntegerField()
    value = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    class Meta:
        app_label = 'celse'
        managed = True
        db_table = 'paramlog'
        

