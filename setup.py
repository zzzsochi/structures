# coding: utf8

from distutils.core import setup

# python setup.py bdist_egg
# python setup.py sdist --formats=bztar

from structures import __version__

description = u'User-friendly library for creating data structures.'
long_description = open('README.rst', 'rb').read()


setup(
        name='structures',
        version=__version__,
        description=description,
        long_description=long_description,
        author='Zelenyak Aleksandr aka ZZZ',
        author_email='ZZZ.Sochi@GMail.com',
        url='https://github.com/zzzsochi/structures',
        license='GPL',
        platforms='any',

        classifiers=[
                'Development Status :: 5 - Production/Stable',
                'Intended Audience :: Developers',
                'Operating System :: OS Independent',
                'Programming Language :: Python',
                'Programming Language :: Python :: 2.5',
                'Programming Language :: Python :: 2.6',
                'Programming Language :: Python :: 2.7',
              ],

        packages=['structures'],
    )
