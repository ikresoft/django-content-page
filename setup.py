#!/usr/bin/env python

from setuptools import setup, find_packages
github_url = 'https://github.com/ikresoft/django-content-page'


setup(
    name='django-content-page',
    version='1.0',
    description='Django page content',
    long_description='Django page content',
    author='Enver Bisevac, Mirza Delic',
    author_email='ikresoft@gmail.com',
    url=github_url,
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django, Django Page Content',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    zip_safe=False,
)
