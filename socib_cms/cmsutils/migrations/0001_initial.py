# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField()),
                ('order', models.IntegerField(default=100, verbose_name='order')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LinkSet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=20, verbose_name='code')),
                ('description', models.CharField(max_length=200, null=True, verbose_name='description', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='URLLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_ca', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_es', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('description', models.CharField(max_length=900, null=True, verbose_name='description', blank=True)),
                ('description_en', models.CharField(max_length=900, null=True, verbose_name='description', blank=True)),
                ('description_ca', models.CharField(max_length=900, null=True, verbose_name='description', blank=True)),
                ('description_es', models.CharField(max_length=900, null=True, verbose_name='description', blank=True)),
                ('css_class', models.CharField(max_length=50, null=True, verbose_name='CSS class', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('created_by', models.ForeignKey(related_name='created-urllink', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by')),
                ('picture', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='picture', blank=True, to='filer.Image', null=True)),
                ('updated_by', models.ForeignKey(related_name='updated-urllink', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='update by')),
            ],
            options={
                'verbose_name': 'URL link',
                'verbose_name_plural': 'URL links',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='genericlink',
            name='linkset',
            field=models.ForeignKey(to='cmsutils.LinkSet'),
            preserve_default=True,
        ),
    ]
