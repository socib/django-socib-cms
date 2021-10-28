# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
    migrations.AddField(
        model_name='page',
        name='skip_old_website',
        field=models.BooleanField(default=False, verbose_name='Do not update page from old website'),
        preserve_default=False,
    ),
    migrations.AddField(
        model_name='page',
        name='created_on',
        field=models.BooleanField(default=True, verbose_name='show section menu'),
        preserve_default=False,
    ),
    migrations.AddField(
        model_name='page',
        name='updated_on',
        field=models.DateTimeField(auto_now=True, verbose_name='date modified'),
        preserve_default=False,
    ),
    migrations.AddField(
        model_name='page',
        name='created_by',
        field=models.ForeignKey(related_name='created-page', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by'),
        preserve_default=False,
    ),
    migrations.AddField(
        model_name='page',
        name='updated_by',
        field=models.ForeignKey(related_name='updated-page', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='update by'),
        preserve_default=False,
    )
    ]