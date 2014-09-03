#!/bin/env python
# -*- coding: utf-8 -*-

'''Django package for bootstrap:
a sleek, intuitive, and powerful front-end framework
for faster and easier web development'''

from setuptools import setup

setup(
    name='django-bootstrap',
    version='3.2.0',
    url='http://getbootstrap.com',
    description=globals()['__doc__'],
    author='Mark Otto, Jacob Thornton',
    maintainer='Renat Galimov',
    maintainer_email='renat2017@gmail.com',
    license='MIT License',
    keywords=['django', 'bootstrap'],
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    packages=['django_bootstrap'],
    package_data={
        'django_bootstrap':
        ['static/django_bootstrap/js/*',
         'static/django_bootstrap/css/*',
         'static/django_bootstrap/fonts/*',]
    }
)
