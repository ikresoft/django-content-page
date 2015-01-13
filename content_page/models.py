#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module provides the Page model for reporting news, events, info etc.
"""

from django.conf import settings as site_settings
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from django.db import models
from django.utils.translation import ugettext as _
from content import settings
from content.models import Content


class Page(Content):
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name=_(u'Parent'))
    template = models.CharField(max_length=100, null=True, blank=True, verbose_name=_(u'Template'))

    def get_slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse('page_detail', args=tuple(), kwargs={
            'slug': self.slug
        })


# Reversion integration
if settings.USE_REVERSION:
    rev_error_msg = 'Pages excepts django-reversion to be '\
                    'installed and in INSTALLED_APPS'
    try:
        import reversion
        if not 'reversion' in site_settings.INSTALLED_APPS:
            raise ImproperlyConfigured(rev_error_msg)
    except (ImportError, ):
        raise ImproperlyConfigured(rev_error_msg)

    reversion.register(Page)
