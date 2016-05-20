# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ctrls',
            fields=[
                ('idctrls', models.IntegerField(serialize=False, primary_key=True)),
                ('bus_id', models.IntegerField()),
                ('online', models.IntegerField(null=True, blank=True)),
                ('type', models.IntegerField()),
                ('description', models.CharField(max_length=45, blank=True)),
                ('last_update', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'ctrls',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parametrs',
            fields=[
                ('idparametrs', models.IntegerField(serialize=False, primary_key=True)),
                ('bus_id', models.IntegerField()),
                ('addr', models.IntegerField()),
                ('value', models.IntegerField(null=True, blank=True)),
                ('addr_type', models.IntegerField()),
                ('direction', models.IntegerField()),
                ('description', models.CharField(max_length=45, blank=True)),
                ('last_update', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'parametrs',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TCtrl',
            fields=[
                ('idtable1', models.IntegerField(serialize=False, primary_key=True)),
                ('type_id', models.IntegerField()),
                ('description', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'db_table': 't_ctrl',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
