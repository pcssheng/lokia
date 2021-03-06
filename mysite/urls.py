#-*— coding:UTF-8 -*-
#/usr/bin/env python
"""
module descript
"""
import os
from django.conf.urls import patterns, url
from views import *
from click_view import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
this_path = os.path.join(os.path.dirname(__file__), '..')

urlpatterns = patterns('',
    url(r'^text/$', response_msg),
    #click event
    url(r'^event/CLICK/about/$', about),
    url(r'^event/CLICK/contact/$', contact),
    url(r'^event/CLICK/order/$', order),
    url(r'^check_signature/$', check_signature),
    #通用试图
    url(r'^index/$', IndexView.as_view()),
    url(r'^qrcode/$', qr_code),
    url(r'^get_customer_msg/$', get_customer_msg),
    url(r'^customer_msg/$', customer_msg),
    url(r'^test/$', test),
    url(r'^js/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': this_path + '/js/'}),

    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': this_path + '/css/'}),

    url(r'^image/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': this_path + '/image/'}),
    )