# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_split_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='created_by',
            field=models.ForeignKey(related_name='created_page', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by'),
        ),
        migrations.AlterField(
            model_name='page',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_page', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='update by'),
        ),
    ]
