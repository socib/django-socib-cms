django-socib-cms
=====================

This is a simple CMS django application for SOCIB web projects, with hierarchy pages (based on django contrib Flatpages) and news.

This is an evolution of the app grumers.apps.web (see https://github.com/socib/grumers), modified to make it reusable for other projects. It might have too many requirements, that should be optional (TODO).


Quick start
-----------

1. Add "socib_cms", "socib_cms.pages", "socib_cms.news" and current required apps to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = (
        ...
        'socib_cms',
        'socib_cms.pages',
        'socib_cms.news',
        # required apps
        'ckeditor_filer',
        'compressor',
        'envelope',
        'mptt',
        'django_tables2',
        'crispy_forms',
        'localeurl',
        'modeltranslation',
        'filer',
        'easy_thumbnails',
        'password_reset',
        'admin_shortcuts',
        'djangocms_admin_style',
        'taggit',
        'django.contrib.sites',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.flatpages',
        'django.contrib.humanize',
        ...
        # optional, but recommended
        'south',
    )

2. Configure mandatory settings for the apps::

    SOUTH_MIGRATION_MODULES = {
        'easy_thumbnails': 'easy_thumbnails.south_migrations',
        'taggit': 'taggit.south_migrations',
    }

    TEMPLATE_CONTEXT_PROCESSORS += (
        'django.core.context_processors.request',
        'django.core.context_processors.i18n',
    )

    MIDDLEWARE_CLASSES += (
        'localeurl.middleware.LocaleURLMiddleware',
    )

    CRISPY_TEMPLATE_PACK = 'bootstrap3'
    ADMIN_SHORTCUTS_SETTINGS = {
        'hide_app_list': False,
        'open_new_window': False,
    }

    ADMIN_SHORTCUTS = [
        {
            'title': _('Website'),
            'shortcuts': [
                {
                    'url': '/',
                    'open_new_window': True,
                },
            ]
        },
    ]

    THUMBNAIL_PROCESSORS = (
        'easy_thumbnails.processors.colorspace',
        'easy_thumbnails.processors.autocrop',
        'filer.thumbnail_processors.scale_and_crop_with_subject_location',
        'easy_thumbnails.processors.filters',
    )

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
        # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
        'compressor.finders.CompressorFinder',
    )

    COMPRESS_ROOT = STATIC_ROOT
    COMPRESS_URL = STATIC_URL
    COMPRESS_OUTPUT_DIR = 'CACHE'
    COMPRESS_PRECOMPILERS = (
        ('text/less', 'lessc {infile} {outfile}'),
    )

    MODELTRANSLATION_PREPOPULATE_LANGUAGE = 'en'
    MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
    MODELTRANSLATION_FALLBACK_LANGUAGES = {
        'default': ('en', 'ca', 'es'),
        'ca': ('es',),
        'es': ('ca',),
    }

3. Include socib_cms URLconf in your project urls.py like this::

    url(r'^', include('socib_cms.urls')),

4. Run `python manage.py migrate` to create the models (pages and news).

