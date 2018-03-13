try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config  = {
  'description': 'a python side project',
  'author': 'chafel',
  'url': 'https://github.com/chafel/laghing',
  'version': '0.0',
  'install_requires': ['nose'],
  'packages': ['bin', 'NAME'],
  'scripts': ['./bin/hello'],
  'name': 'laughing'
}

setup(**config)