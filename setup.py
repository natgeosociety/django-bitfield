#!/usr/bin/env python
import os
import sys
from setuptools import setup, find_packages

version = __import__('bitfield').get_version()

if sys.argv[-1] == 'publish':
    os.system('python setup.py bdist_wheel upload -r natgeo')
    print("You probably want to also tag the version now:")
    print("  python setup.py tag")
    sys.exit()
elif sys.argv[-1] == 'tag':
    cmd = "git tag -a %s -m 'version %s';git push --tags" % (version, version)
    os.system(cmd)
    sys.exit()


setup(
    name='django-bitfield-ng',
    version=version.replace(' ', '-'),
    author='Disqus',
    author_email='opensource@disqus.com',
    url='https://github.com/disqus/django-bitfield',
    description='BitField in Django',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'six',
    ],
    extras_require={
        'tests': [
            'flake8',
            'mysqlclient',
            'psycopg2>=2.3',
            'pytest-django',
        ],
    },
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
