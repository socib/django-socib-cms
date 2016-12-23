# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.folder
import filer.fields.file
import filer.fields.image
import django.db.models.deletion
from django.conf import settings
import socib_cms.utils
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publish_date', models.DateField(verbose_name='publishing date')),
                ('is_draft', models.BooleanField(default=True, verbose_name='draft')),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_ca', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_es', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('content', models.TextField(verbose_name='content', blank=True)),
                ('content_en', models.TextField(null=True, verbose_name='content', blank=True)),
                ('content_ca', models.TextField(null=True, verbose_name='content', blank=True)),
                ('content_es', models.TextField(null=True, verbose_name='content', blank=True)),
                ('introduction', models.CharField(max_length=900, null=True, verbose_name='Introduction', blank=True)),
                ('introduction_en', models.CharField(max_length=900, null=True, verbose_name='Introduction', blank=True)),
                ('introduction_ca', models.CharField(max_length=900, null=True, verbose_name='Introduction', blank=True)),
                ('introduction_es', models.CharField(max_length=900, null=True, verbose_name='Introduction', blank=True)),
                ('redirect_link', models.CharField(max_length=300, null=True, verbose_name='redirect link', blank=True)),
                ('slug', models.CharField(max_length=100, verbose_name='slug')),
                ('css_class', models.CharField(max_length=50, null=True, verbose_name='CSS class', blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('album', filer.fields.folder.FilerFolderField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='album', blank=True, to='filer.Folder', null=True)),
                ('attachment', filer.fields.file.FilerFileField(related_name='news_attachment', on_delete=django.db.models.deletion.SET_NULL, verbose_name='attachment', blank=True, to='filer.File', null=True)),
            ],
            options={
                'ordering': ('-publish_date',),
                'verbose_name': 'news',
                'verbose_name_plural': 'news',
            },
            bases=(models.Model, socib_cms.utils.ClonableMixin),
        ),
        migrations.CreateModel(
            name='NewsCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('name_en', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('name_ca', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('name_es', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('slug', models.CharField(unique=True, max_length=100, verbose_name='slug')),
                ('hide_cat_menu', models.BooleanField(default=False, verbose_name='Hide in categories menu')),
            ],
            options={
                'verbose_name': 'news category',
                'verbose_name_plural': 'news categories',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='news',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='category', to='news.NewsCategory'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='created_by',
            field=models.ForeignKey(related_name='created-news', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='created by'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='picture',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='picture', blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='related',
            field=models.ManyToManyField(related_name='related_rel_+', null=True, verbose_name='related news', to='news.News', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='updated_by',
            field=models.ForeignKey(related_name='updated-news', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True, verbose_name='update by'),
            preserve_default=True,
        ),
    ]
