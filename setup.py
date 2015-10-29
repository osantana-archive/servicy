#!/usr/bin/env python
# coding: utf-8


import re


try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command


def get_version(filename):
    with open(filename) as changelog:
        for line in changelog:
            version = re.search(r'^[0-9]+\.[0-9]+(\.[0-9]+)?', line)
            if version:
                version = version.group()
                break
        else:
            version = "0.0.0"
    return version


def load(filename):
    with open(filename) as file_:
        return file_.read()


def load_requirements(filename):
    requirements = []
    with open(filename) as reqfile:
        for line in reqfile:
            line = line.strip()
            if not line.startswith("-r "):
                requirements.append(line)
                continue
            filename = line.split(maxsplit=1)[-1]
            requirements.extend(load_requirements(filename))
    return requirements


class VersionCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(get_version("CHANGES.rst"))


setup(
    name='servicy',
    version=get_version("CHANGES.rst"),
    description="Library for reliable HTTP service integrations",
    long_description=load('README.rst') + '\n\n' + load('CHANGES.rst').replace('.. :changelog:', ''),
    author="Osvaldo Santana Neto",
    author_email='servicy@osantana.me',
    url='https://github.com/osantana/servicy',
    packages=[
        'servicy',
    ],
    include_package_data=True,
    install_requires=load_requirements("requirements.txt"),
    license="MIT",
    zip_safe=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
    ],
    test_suite='tests',
    tests_require=load_requirements("requirements-dev.txt"),
    cmdclass={"version": VersionCommand},
)
