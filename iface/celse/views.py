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
#from iface.forms import SetpointForm
# must be installed !!!! from qsstats import QuerySetStats
#from django.core.context_processors import request

def main(request):
    current_date = datetime.datetime.now()
    t_ctrl = models.TCtrl.objects.all()
    ctrl = models.Ctrls.objects.all()
    param = models.Parametrs.objects.all()
#    param = models.Parametrs.objects.filter(addr=0 | addr=7 | addr=6 | addr=3 | addr=257)
#    p_error_ds = float(param[2].value)/float(param[3].value)
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
        ctrl = models.Ctrls.objects.filter(bus_id=req_bus_id)
        param = models.Parametrs.objects.filter(bus_id=req_bus_id)
        return render_to_response('celse/ctrl_details.html', locals())
    else :
        render_to_response('celse/current_data.html', locals())

def system_config (request):
    current_date = datetime.datetime.now()
    if request.method == 'GET':
        form = SetpointForm(request.GET)
    if form.is_valid():
        params = models.Parametrs.objects.filter(addr=1)
        for param in params:
            param.value = float(request.GET['value'])
            param.save()
#        param.save()
    else:
        param = models.Parametrs.objects.filter(addr=1)[0]
        form = SetpointForm(initial = {'description':  'Температура на входе в чиллер',
                                   'value': param.value,
                                   })
    return render_to_response('celse/config.html', locals())

def scripts(request, name):
    data = open(os.path.join('scripts',name), 'rb').read()

    return HttpResponse(data)