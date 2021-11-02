# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20161202_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='NewsCategory',
            name='hide_cat_menu',
            field=models.BooleanField(default=False, verbose_name='Hide in categories menu'),
            preserve_default=False,
        ),
    ]
