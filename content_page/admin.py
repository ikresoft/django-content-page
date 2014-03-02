#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings as site_settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from content import settings
from models import Page
from forms import PageForm

from content.admin import ChildAdmin

class PageAdmin(ChildAdmin):
    base_model = Page
    fieldsets = (
        (None, {
            'fields': ('title', 'template', 'body')
        }),
        (_('Page data'), {
            'fields': ('authors', 'non_staff_author',
                       'status', 'origin', 'comment_status', )
        }),)

    if settings.INCLUDE_PRINT:
        fieldsets = fieldsets + (_('Print Information'), {
            'fields': ('print_pub_date', 'print_section', 'print_page'),
            'classes': ('collapse',),
        })

    fieldsets = fieldsets + ((_('Advanced Options'), {
            'fields': ('slug', ('publish_date', 'publish_time'),
                       'update_date', 'site', ),
            'classes': ('collapse',),
        }),)
    form = PageForm

