from __future__ import unicode_literals
from setuptools import setup, find_packages

setup(name='gem-mirator',
      version = '0.1.0',
      description = 'utility for migrating Gem application wallets',
      url = 'http://github.com/GemHQ/gem-migrator',
      author = 'Matt Smith',
      author_email = 'matt@gem.co',
      license = 'MIT',
      packages = find_packages(),
      install_requires = [
          'PyNaCl==0.3.0',
          'round',
#         'round==0.8.1',
      ],
      tests_require = [ 'tox' ],
      scripts=['migrate.py'],
      zip_safe=False)
