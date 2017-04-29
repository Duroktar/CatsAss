import sys
import os
from setuptools import setup, find_packages


SETUP_DIR = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(SETUP_DIR, 'README.rst')) as f:
    long_description = f.read()

__version__ = '1.1.1'


# From https://www.pydanny.com/python-dot-py-tricks.html
if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    os.system("python setup.py bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (__version__, __version__))
    print("  git push --tags")
    sys.exit()


if sys.argv[-1] == 'build':
    os.system("python setup.py sdist")
    os.system("python setup.py bdist_wheel")
    sys.exit()

setup(
    name='CatsAss',
    version=__version__,
    packages=find_packages(exclude=['docs', 'images']),
    package_data={
        'catsass': ['logo', 'octocat']
    },
    description='Seriously the cats ass. Seriously.',
    long_description=long_description,
    url='https://pypi.python.org/pypi/CatsAss',
    author="Duroktar",
    author_email='duroktar@gmail.com',
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Software Development :: Debuggers',
        'Topic :: Games/Entertainment :: Fortune Cookies',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
