#!/usr/bin/env python

from setuptools import setup, find_packages

version = __import__('socib_cms').__version__

setup(
    name='django-socib-cms',
    version=version,
    description='Django SOCIB CMS',
    long_description='Simple CMS for SOCIB projects',
    author='Biel Frontera',
    author_email='data.centre@socib.es',
    url='https://github.com/socib/django-socib-cms',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    install_requires=(
        'Django==1.9.12',
        'Pillow',
        'easy-thumbnails',
        'django-mptt',  # 0.6 to 0.8.6
        'django-modeltranslation',
        'django-password-reset',
        'django-filer',  # 0.9.12 to 1.2.5
        'django-taggit',  # 0.12 to 0.21.3
        'djangocms-admin-style',  # 0.2.8 to 1.2.6.2
        'django-admin-shortcuts',
        'python-ldap',
        'django-auth-ldap',
        'django-envelope',  # 0.7 to 1.7
        'django-honeypot',
        'django-crispy-forms',
        'django-tables2',  # 0.15.0 to 1.2.6
        'django_compressor',
        'django-ace',
        # 'django-genericadmin',  # 0.6.1 < github.com/arthanson/django-genericadmin
        'elasticsearch==1.9.0',  # 2.0 is not compatible with mlt
        'haystack',  # 0.15 to 0.36
        'django-haystack',  # 2.3.1 to 2.5.1
        'django-ckeditor',
        'django-ckeditor-filebrowser-filer'
    ),
    dependency_links=[
        'git+https://github.com/arthanson/django-genericadmin.git#egg=django_genericadmin-0.6.1'
    ],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
