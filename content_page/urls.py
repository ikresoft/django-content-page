#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""URL definitions for news pages
"""
try:
    from django.conf.urls.defaults import patterns, url
except ImportError:
    from django.conf.urls import patterns, url

urlpatterns = patterns('',
    #page detail
    url(
        r'^(?P<slug>[-\w]+)/$',
        'content_page.views.page_detail',
        name='page_detail'
    ),

)
