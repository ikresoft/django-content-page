#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import Http404
from django.shortcuts import render_to_response
from django.template import RequestContext

from content import settings
from models import Page


def page_detail(request, slug, extra_context={}):
    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        if not settings.THROW_404:
            return render_to_response('content_page/removed.html',
                                      {},
                                      context_instance=RequestContext(request))
        else:
            raise Http404
    context = {
        'page': page,
    }
    if extra_context:
        context.update(extra_context)
    if page.template == "":
        template_name = "content_page/detail.html"
    return render_to_response(template_name, context,
                              context_instance=RequestContext(request))

