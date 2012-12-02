from distutils.core import setup

# python setup.py bdist_egg
# python setup.py sdist --formats=bztar

from structures import __version__

description = 'User-friendly library for creating data structures.'
long_description = open('README.rst', 'rb').read().decode('utf8')


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
                'Programming Language :: Python :: 3',
                'Programming Language :: Python :: 3.2',
                'Programming Language :: Python :: 3.3',
              ],

        packages=['structures'],
    )
