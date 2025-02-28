from setuptools import setup

VERSION = '0.4.5'

install_requires = [
    "arrow==1.3.0",
    "cassandra-driver==3.29.2",
    "click==8.1.8",
    "future==1.0.0",
    "geomet==0.2.1.post1",
    "python-dateutil==2.9.0.post0",
    "PyYAML==6.0.1",
    "six==1.17.0",
    "tabulate==0.9.0",
    "typing-extensions==4.12.2"]

setup(name='cassandra-migrate',
      packages=['cassandra_migrate'],
      version=VERSION,
      description='Simple Cassandra database migration program.',
      long_description=open('README.rst').read(),
      url='https://github.com/Cobliteam/cassandra-migrate',
      license='MIT',
      install_requires=install_requires,
      scripts=['bin/cassandra-migrate'],
      keywords='cassandra schema migration')
