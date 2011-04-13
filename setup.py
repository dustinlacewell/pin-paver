import os

from setuptools import setup

setup(
    name='pinpaver',
    version='0.1rc1',
    packages=['pin','pin.plugins'],
    namespace_packages=['pin', 'pin.plugins'],
    install_requires=['paver'],
    provides=['pinpaver'],
    author='Dustin Lacewell',
    author_email='dlacewell@gmail.com',
    url='https://github.com/dustinlacewell/pin-fabric',
    description="Paver plugins for pin",
    long_description=open('README.markdown').read(),
)
