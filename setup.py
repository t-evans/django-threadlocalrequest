#!/usr/bin/env python
# User: Troy Evans
# Date: 1/24/13
# Time: 8:54 PM
#
# Copyright 2012, Nutrislice Inc.  All rights reserved.
from distutils.core import setup
import threadlocalrequest


def read_files(*filenames):
    """
    Output the contents of one or more files to a single concatenated string.
    """
    output = []
    for filename in filenames:
        f = open(filename)
        try:
            output.append(f.read())
        finally:
            f.close()
    return '\n\n'.join(output)


setup(
    name='threadlocalrequest',
    version=threadlocalrequest.VERSION,
    url='https://github.com/t-evans/django-threadlocalrequest.git',
    description='Contains middleware for placing the current Django request in threadlocal storage.',
    long_description=read_files('README.md'),
    author='Troy Evans',
    author_email='troy@nutrislice.com',
    platforms=['any'],
    packages=[
        'threadlocalrequest',
    ],
    #package_data={'threadlocalrequest': ['docs/*', 'docs/ref/*.rst']},
    classifiers=[
        'Development Status :: Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    zip_safe=False,
)
