"""
termcc
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='termcc',
    version='2018.11.03',
    url='https://github.com/pingf/termcc.git',
    license='BSD',
    author='dameng',
    author_email='pingf0@gmail.com',
    description='give you some color to see see(chinese idiom) in terminal',
    long_description=__doc__,
    py_modules=['termcc'],
    # if you would be using a package instead use packages instead
    # of py_modules:
    packages=['termcc'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
    ],
    scripts=['bin/cc.py'],
    entry_points={'console_scripts': [
        'termcc = termcc_show:show',
    ]},
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)