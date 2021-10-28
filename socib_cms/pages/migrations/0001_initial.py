# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.folder
import mptt.fields
import django.db.models.deletion
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('filer', '0006_auto_20160623_1627'),
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('flatpage_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='flatpages.FlatPage')),
                ('title_en', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_ca', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('title_es', models.CharField(max_length=200, null=True, verbose_name='title')),
                ('content_en', models.TextField(null=True, verbose_name='content', blank=True)),
                ('content_ca', models.TextField(null=True, verbose_name='content', blank=True)),
                ('content_es', models.TextField(null=True, verbose_name='content', blank=True)),
                ('title_menu', models.CharField(max_length=50, verbose_name='Short title for menu')),
                ('title_menu_en', models.CharField(max_length=50, null=True, verbose_name='Short title for menu')),
                ('title_menu_ca', models.CharField(max_length=50, null=True, verbose_name='Short title for menu')),
                ('title_menu_es', models.CharField(max_length=50, null=True, verbose_name='Short title for menu')),
                ('order', models.IntegerField(default=0, verbose_name='order')),
                ('introduction', models.CharField(help_text='This text will be used in lists. If empty, the system will use the first 20 words of content', max_length=900, null=True, verbose_name='Introduction', blank=True)),
                ('introduction_en', models.CharField(help_text='This text will be used in lists. If empty, the system will use the first 20 words of content', max_length=900, null=True, verbose_name='Introduction', blank=True)),
                ('introduction_ca', models.CharField(help_text='This text will be used in lists. If empty, the system will use the first 20 words of content', max_length=900, null=True, verbose_name='Introduction', blank=True)),
                ('introduction_es', models.CharField(help_text='This text will be used in lists. If empty, the system will use the first 20 words of content', max_length=900, null=True, verbose_name='Introduction', blank=True)),
                ('extra_content', models.TextField(verbose_name='extra content', blank=True)),
                ('extra_content_en', models.TextField(null=True, verbose_name='extra content', blank=True)),
                ('extra_content_ca', models.TextField(null=True, verbose_name='extra content', blank=True)),
                ('extra_content_es', models.TextField(null=True, verbose_name='extra content', blank=True)),
                ('is_container', models.BooleanField(default=False, verbose_name='page is just a container')),
                ('hide', models.BooleanField(default=False, verbose_name='hide this page in lists')),
                ('list_children', models.BooleanField(default=False, verbose_name='list children pages inside this page content')),
                ('include_children', models.BooleanField(default=False, verbose_name='children pages content is shown in sections of this page')),
                ('picture_description', models.CharField(max_length=900, null=True, verbose_name='picture description', blank=True)),
                ('picture_description_en', models.CharField(max_length=900, null=True, verbose_name='picture description', blank=True)),
                ('picture_description_ca', models.CharField(max_length=900, null=True, verbose_name='picture description', blank=True)),
                ('picture_description_es', models.CharField(max_length=900, null=True, verbose_name='picture description', blank=True)),
                ('picture_location', models.CharField(default=b'extra', max_length=10, verbose_name='picture location', choices=[(b'header', 'Header'), (b'extra', 'Inside extra content'), (b'background', 'As background image'), (b'none', 'Do not show')])),
                ('js_code', models.TextField(verbose_name='javascript code', blank=True)),
                ('css_class', models.CharField(max_length=50, null=True, verbose_name='CSS class', blank=True)),
                ('css_container_style', models.CharField(max_length=300, null=True, verbose_name='CSS styles', blank=True)),
                ('old_url', models.CharField(max_length=255, null=True, verbose_name='Old URL', blank=True)),
                ('skip_old_website', models.BooleanField(default=False, verbose_name='Do not update page from old website')),
                ('redirect_link', models.CharField(max_length=300, null=True, verbose_name='redirect link', blank=True)),
                ('content_template_name', models.CharField(help_text="Example: 'pages/content/intro.html'. If this isn't provided, the system will use 'pages/content/default.html'.", max_length=70, verbose_name='content template name', blank=True)),
                ('content_columns', models.IntegerField(default=12, verbose_name='content columns')),
                ('extra_content_columns', models.IntegerField(default=4, verbose_name='extra content columns')),
                ('float_extra_content', models.BooleanField(default=True, verbose_name='float extra content')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('album', filer.fields.folder.FilerFolderField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='album', blank=True, to='filer.Folder', null=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='parent', blank=True, to='pages.Page', null=True)),
                ('picture', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, verbose_name='picture', blank=True, to='filer.Image', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('flatpages.flatpage', models.Model),
        ),
    ]
