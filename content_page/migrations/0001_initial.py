# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('content_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='content.Content')),
                ('template', models.CharField(max_length=100, null=True, verbose_name='Template', blank=True)),
                ('parent', models.ForeignKey(verbose_name='Parent', blank=True, to='content_page.Page', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('content.content',),
        ),
    ]
