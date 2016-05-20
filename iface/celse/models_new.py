# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Ctrls(models.Model):
    idctrls = models.IntegerField(unique=True)
    bus_id = models.IntegerField()
    online = models.IntegerField(blank=True, null=True)
    type = models.IntegerField()
    description = models.CharField(max_length=100, blank=True)
    last_update = models.DateTimeField(blank=True, null=True)
    class Meta:
        app_label = 'celse'
        managed = True
        db_table = 'ctrls'


class Parametrs(models.Model):
    idparametrs = models.IntegerField(unique=True)
    bus_id = models.IntegerField()
    addr = models.IntegerField()
    value = models.FloatField(blank=True, null=True)
    to_log = models.IntegerField()
    description = models.CharField(max_length=45, blank=True)
    last_update = models.DateTimeField(blank=True, null=True)
    addr_type = models.IntegerField()
    direction = models.IntegerField()
    to_set = models.IntegerField()
    class Meta:
	app_label = 'celse'
        managed = True
        db_table = 'parametrs'

class Paramlog(models.Model):
    idparamlog = models.IntegerField(unique=True)
    bus_id = models.IntegerField()
    addr = models.IntegerField()
    addr_type = models.IntegerField()
    value = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    class Meta:
        app_label = 'celse'
        managed = True
        db_table = 'paramlog'

class TCtrl(models.Model):
    idtable1 = models.IntegerField(unique=True)
    type_id = models.IntegerField()
    description = models.CharField(max_length=45, blank=True)
    class Meta:
        app_label = 'celse'
        managed = True
        db_table = 't_ctrl'

