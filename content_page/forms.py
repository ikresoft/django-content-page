#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime

from django import forms
from django.utils.translation import ugettext as _

from models import Page
from content.forms import ContentForm

class PageForm(ContentForm):
    class Meta:
    	model = Page
    	exclude = ('categories',)

