#!/usr/bin/env python

from setuptools import setup

version = '0.1.0'

install_requires = [
    'click',
    'polib'
]
setup(
    name='candy_i18n',
    version=version,
    description='Smart internationalization library for Python',
    long_description=open('README.md').read(),
    author='Fay Cheng',
    author_email='fay.cheng.cn@gmail.com',
    url='https://gihub.com/faycheng/candy_i18n',
    install_requires=install_requires,
    license='MIT',
    packages=['candy_i18n'],
    py_modules=['cli'],
    entry_points={
         'console_scripts': ['candy_i18n=cli:cli']},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)