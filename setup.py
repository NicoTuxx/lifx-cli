"""Packaging settings."""


from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from lifx import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as readme_file:
    readme = readme_file.read()

with open(join(this_dir, 'HISTORY.rst'), encoding='utf-8') as history_file:
    history = history_file.read()

long_description = '%s /n/n %s' % (readme, history)

class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=lifx', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name = 'lifx',
    version = __version__,
    description = 'LifX-cli is a command line interface to control your lifx bulbs, based on the `lifxlan` python module.',
    long_description = long_description,
    url = 'https://github.com/NicoTuxx/lifx-cli',
    author = 'NicoTuxx',
    author_email = 'dev@nicotuxx.co',
    license = 'MIT',
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    keywords = 'lifx-cli',
    packages = find_packages(exclude=['docs', 'tests*']),
    install_requires = [
        'docopt',
        'lifxlan'
    ],
    extras_require = {
        'test': [
            'coverage',
            'pytest',
            'pytest-cov'
        ],
    },
    entry_points = {
        'console_scripts': [
            'lifx=lifx.cli:main',
        ],
    },
    cmdclass = {'test': RunTests},
)
