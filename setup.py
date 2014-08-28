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
        'Django>=1.4',
        'Pillow',
        'easy-thumbnails>=1.0',
        'django-mptt',
        'django-localeurl',
        'django-modeltranslation',
        'django-password-reset',
        'django-filer',
        'django-taggit',
        'djangocms-admin-style',
        'django-admin-shortcuts',
        'python-ldap',
        'django-auth-ldap',
        'django-envelope',
        'django-honeypot',
        'django-crispy-forms',
        'django-tables2',
        'django_compressor',
        'ckeditor_filer',
        'django-ace'
    ),
    dependency_links=[
        'git+https://github.com/bielfrontera/django-ckeditor-filer.git#egg=ckeditor_filer-1.0'
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
