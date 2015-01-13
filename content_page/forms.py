#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models import Page
from content.forms import ContentForm


class PageForm(ContentForm):

    class Meta:
        model = Page
        fields = "__all__"
