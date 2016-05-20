#!/usr/bin/python
# -*- coding: utf-8 -*-
#from django.conf.urls.defaults import *
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
#from celse import models
#from django.views.generic import list_detail

from celse import views

#ctrl_info = {
#    'queryset': models.Parametrs.objects.all(),
#    'template_name': 'ctrl_details.html',
#}

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'iface.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^scripts/([^/]+)$','scripts'),
    url(r'^$', views.main),
    url(r'^ctrl_details/$', views.ctrl_details),
    url(r'^config/$', views.system_config),
    url(r'^admin/', include(admin.site.urls)),


) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#urlpatterns += staticfiles_urlpatterns()

#urlpatterns = i18n_patterns("",
# ...
#    url(r"^js-settings/$", "iface.views.render_js",{"template_name": 'settings.js'}, name="js_settings"),
#)
