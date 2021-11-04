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
        'Django>=1.10,<2.0',
        'Pillow',
        'easy-thumbnails',
        'django-mptt==0.9.1',  # 0.6 to 0.8.6
        'django-modeltranslation==0.14.4',
        'django-polymorphic==2.1.2',
        'django-password-reset==1.0',
        'django-filer==1.7.1',  # 0.9.12 to 1.2.5
        'django-taggit==0.24.0',  # 0.12 to 0.21.3
        'djangocms-admin-style',  # 0.2.8 to 1.2.6.2
        'django-admin-shortcuts',
        'python-ldap',
        'django-auth-ldap==1.2.1',
        'django-envelope==1.4.0',  # 0.7 to 1.7
        'django-honeypot',
        'django-crispy-forms<1.9.0',
        'django-tables2==2.0.6',  # 0.15.0 to 1.2.6
        'django-appconf<1.0.4',
        'django_compressor',
        'django-ace==1.0.3',
        # 'django-genericadmin',  # 0.6.1 < github.com/arthanson/django-genericadmin
        'elasticsearch==1.9.0',  # 2.0 is not compatible with mlt
        'haystack',  # 0.15 to 0.36
        'django-haystack==2.7.0',  # 2.3.1 to 2.5.1
        'django-ckeditor<6.0.0',
        'django-ckeditor-filebrowser-filer',
        'packaging',
        'appdirs'
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
