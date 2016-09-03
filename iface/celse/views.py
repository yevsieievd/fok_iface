#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 27 лют. 2016

@author: dbe
'''
import os

from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from celse import models
from qsstats import QuerySetStats
from django.db.models import Avg
from datetime import timedelta

#from iface.forms import SetpointForm
#from django.core.context_processors import request

def main(request):
    current_date = datetime.datetime.now()
    t_ctrl = models.TCtrl.objects.all()
    ctrl = models.Ctrls.objects.all()
    param = models.Parametrs.objects.all()
    for par in param:
        if (par.bus_id == 1 and par.addr == 2):
            fun_hc = par.value
    return render_to_response('celse/main.html', locals())

def ctrl_details(request):
    current_date = datetime.datetime.now()
    if 'req_bus_id' in request.GET and request.GET['req_bus_id']:
        req_bus_id = request.GET['req_bus_id']
        ctrl = models.Ctrls.objects.get(bus_id=req_bus_id)
        if 'setpoint' in request.GET and request.GET['setpoint']:
            if ctrl.type == 1:
                sp = models.Parametrs.objects.filter(addr=1)
                for sp in sp:
                    sp.value = float(request.GET['setpoint'])
                    sp.save()
            if ctrl.type == 2:
                sp = models.Parametrs.objects.get(bus_id=req_bus_id, addr=4)
                sp.value = float(request.GET['setpoint'])
                sp.save()
            if ctrl.type == 3:
                sp = models.Parametrs.objects.get(bus_id=req_bus_id, addr=0)
                sp.value = float(request.GET['setpoint'])
                sp.save()

        if 'mode' in request.GET and request.GET['mode']:
            if ctrl.type == 1:
                mode = models.Parametrs.objects.get(bus_id=req_bus_id, addr=6)
                mode.value = int(request.GET['mode'])
                mode.save()
            if ctrl.type == 2:
                mode = models.Parametrs.objects.get(bus_id=req_bus_id, addr=2)
                mode.value = int(request.GET['mode'])
                mode.to_set = 1;
                mode.save()
            if ctrl.type == 3:
                mode = models.Parametrs.objects.get(bus_id=req_bus_id, addr=1)
                mode.value = int(request.GET['mode'])
                mode.to_set = 1;
                mode.save()
        if 'speed'in request.GET and request.GET['speed']:
            if ctrl.type == 3:
                mode = models.Parametrs.objects.get(bus_id=req_bus_id, addr=3)
                mode.value = int(request.GET['speed'])
                mode.to_set = 1;
                mode.save()
        #ctrl = models.Ctrls.objects.filter(bus_id=req_bus_id)
        param = models.Parametrs.objects.filter(bus_id=req_bus_id)
        if ctrl.type == 3:
            ctrl_mode = param[1].value
            fan_hc = param[2].value
            for par in param:
                if par.addr == 2:
                    fan_hc = par.value
        #logparam = models.Paramlog.objects.filter(bus_id=1, addr=0).order_by('time')
        ##logparam = models.Paramlog.objects.filter(bus_id=1, addr=0).values_list('time', 'value' ).order_by('time')
        #start_date = logparam.first().time
        ##end_date = logparam.last().time
        #end_date = start_date + datetime.timedelta(hours=3)
        #qsstats = QuerySetStats(logparam, date_field='time', aggregate=Avg('value'))
        #values = qsstats.time_series(start_date, end_date, interval='minutes', date_field='time')

        values = models.Paramlog.objects.filter(bus_id=req_bus_id, addr=0, time__gte=(datetime.date.today() - timedelta(days=3))).values_list('time', 'value' ).order_by('time')

        return render_to_response('celse/ctrl_details.html', locals())
    else :
        return render_to_response('celse/current_data.html', locals())


def ctrl_internals(request):
    if 'req_bus_id' in request.GET and request.GET['req_bus_id']:
        req_bus_id = request.GET['req_bus_id']
        parametrs = models.Parametrs.objects.filter(bus_id=req_bus_id)
        return render_to_response('celse/ctrl_internals.html', locals())

def ctrl_service(request):
    if 'req_bus_id' in request.GET and request.GET['req_bus_id']:
        req_bus_id = request.GET['req_bus_id']
        ctrl = models.Ctrls.objects.get(bus_id=req_bus_id)
#        if 'fan_hc' in request.GET and request.GET['fan_hc']:
#            if ctrl.type == 3:
#                sp = models.Parametrs.objects.get(bus_id=req_bus_id, addr=2)
#                sp.value = int(request.GET['fan_hc'])
#                sp.save()
        if 't_corr_sam' in request.GET and request.GET['t_corr_sam']:
            if ctrl.type == 3:
                sp = models.Parametrs.objects.get(bus_id=req_bus_id, addr=4)
                sp.value = int(request.GET['t_corr_sam'])
                sp.save()
        if 't_corr_win' in request.GET and request.GET['t_corr_win']:
            if ctrl.type == 3:
                sp = models.Parametrs.objects.get(bus_id=req_bus_id, addr=5)
                sp.value = int(request.GET['t_corr_win'])
                sp.save()

        parametrs = models.Parametrs.objects.filter(bus_id=req_bus_id)
        for parametr in parametrs:
            if parametr.addr == 2:
                fan_hc = parametr.value
            if parametr.addr == 4:
                t_corr_sam = parametr.value
            if parametr.addr == 5:
                t_corr_win = parametr.value
        return render_to_response('celse/ctrl_service.html', locals())


def do_main(request):
    if 'req_bus_id' in request.GET and request.GET['req_bus_id']:
        req_bus_id = request.GET['req_bus_id']
        ctrl = models.Ctrls.objects.get(bus_id=req_bus_id)
        if 'value' in request.GET and request.GET['value']:
            newvalue = request.GET['value']
            if ctrl.type == 4 and 'addr' in request.GET and request.GET['addr']:
                addrnewval = request.GET['addr']
                sp = models.Parametrs.objects.get(bus_id=req_bus_id, addr=addrnewval)
                sp.value = float(request.GET['value'])
                sp.save()
    ctrls = models.Ctrls.objects.filter(type = 4)
    params = models.Parametrs.objects.all()
    return render_to_response('celse/do_main.html', locals())

def srv_main (request):
    if 'fan_hc' in request.GET and request.GET['fan_hc']:
        sp = models.Parametrs.objects.filter(addr=2, bus_id__lt=13)
        for sp in sp:
            sp.value = int(request.GET['fan_hc'])
            sp.save()
    parametrs = models.Parametrs.objects.filter(bus_id=1)
    for parametr in parametrs:
        if parametr.addr == 2:
            fan_hc = parametr.value
    return render_to_response('celse/srv_main.html', locals())

def system_config (request):
    current_date = datetime.datetime.now()
    if request.method == 'GET':
        form = SetpointForm(request.GET)
    if form.is_valid():
        params = models.Parametrs.objects.filter(addr=1)
        for param in params:
            param.value = float(request.GET['value'])
            param.save()
    else:
        param = models.Parametrs.objects.filter(addr=1)[0]
        form = SetpointForm(initial = {'description':  'Температура на входе в чиллер',
                                   'value': param.value,
                                   })
    return render_to_response('celse/config.html', locals())

def scripts(request, name):
    data = open(os.path.join('scripts',name), 'rb').read()

    return HttpResponse(data)
