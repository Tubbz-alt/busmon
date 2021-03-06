# -*- coding: utf-8 -*-

import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

testpkgs=[
]

install_requires=[
    "fedmsg>=0.5.0",
    "python-memcached",
]


setup(
    name='busmon_consumers',
    version='0.4.5',
    description='fedmsg-hub consumers for the busmon webapp',
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    url='http://github.com/ralphbean/busmon',
    license='GPLv2+',
    setup_requires=["PasteScript >= 1.7"],
    paster_plugins=['PasteScript', 'Pylons', 'TurboGears2', 'tg.devtools'],
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=testpkgs,
    entry_points={
        'moksha.consumer': (
            'memcached = busmon_consumers.consumers:MemcachedStuffer',
        ),
    },
    zip_safe=False
)
