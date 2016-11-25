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
        'Pillow',
        'easy-thumbnails>=1.0',
        'django-mptt==0.6',
        'django-localeurl',
        'django-modeltranslation',
        'django-password-reset',
        'django-filer',
        'django-taggit==0.12',
        'djangocms-admin-style',
        'django-admin-shortcuts',
        'python-ldap',
        'django-auth-ldap',
        'django-envelope==0.7',
        'django-honeypot',
        'django-crispy-forms',
        'django-tables2==0.15.0',
        'django_compressor==1.4',
        # 'ckeditor_filer',
        'django-ace',
        'django-genericadmin==0.6.1',
        'elasticsearch==1.3.0',
        'haystack==0.15',
        'django-haystack==2.3.1'
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
