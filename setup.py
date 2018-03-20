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
        'Django==1.6',
        'Pillow==2.5.3',
        'easy-thumbnails==2.1',
        'django-mptt==0.6.1',
        'django-localeurl==2.0.1',
        'django-modeltranslation==0.7.3',
        'django-password-reset==0.7',
        'django-filer==0.9.7',
        'django-taggit==0.12.1',
        'djangocms-admin-style==0.2.2',
        'django-admin-shortcuts==1.2.5',
        'python-ldap==2.4.16',
        'django-auth-ldap==1.2.1',
        'django-envelope==0.7',
        'django-honeypot==0.4.0',
        'django-crispy-forms==1.4.0',
        'django-tables2==0.15.0',
        'django_compressor==1.4',
        # 'ckeditor_filer',
        'django-ace==1.0.1',
        'django-genericadmin==0.6.1'
    ),
    # dependency_links=[
    #     'git+https://github.com/bielfrontera/django-ckeditor-filer.git#egg=ckeditor_filer-1.0'
    # ],
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
