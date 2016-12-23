# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created_by',
            field=models.ForeignKey(related_name='created_news', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by'),
        ),
        migrations.AlterField(
            model_name='news',
            name='related',
            field=models.ManyToManyField(related_name='_news_related_+', verbose_name='related news', to='news.News', blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_news', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='update by'),
        ),
    ]
