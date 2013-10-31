from distutils.core import setup
from setuptools import find_packages

setup(
    name='pyx509',
    version='0.1.3',
    packages=find_packages(),
    license='GNU Library General Public License',
    long_description=open('README').read(),
    install_requires=[
            "pyasn1 >= 0.1.7",
        ],
    zip_safe=False,
)