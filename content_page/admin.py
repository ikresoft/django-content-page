#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.conf import settings as site_settings
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from content import settings
from models import Page
from forms import PageForm

from content.admin import ContentAdmin

class PageAdmin(ContentAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'parent', 'template',)
        }),
        (_('Content'), {
            'fields': ('body',),
            'classes': ('full-width',),
        }),
        (_('Page data'), {
            'fields': ('authors', 'non_staff_author',
                       'status', 'origin', 'allow_comments', )
        }),)

    fieldsets = fieldsets + ((_('Advanced Options'), {
            'fields': ('slug', 'date_modified', 'site', ),
            'classes': ('collapse',),
        }),)

    form = PageForm

admin.site.register(Page, PageAdmin)
