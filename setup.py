from distutils.core import setup
from setuptools import find_packages

setup(
    name = 'pyx509',
    version = '0.1.4',
    packages = find_packages(),
    scripts = ['bin/x509_parse.py','bin/pkcs7_parse.py'],
    url = 'http://pypi.python.org/pypi/pyx509/',
    license = 'LICENSE.txt',
    description = 'Parse x509v3 certificates and PKCS7 signatures',
    long_description=open('README.txt').read(),
    install_requires=[
            "pyasn1 >= 0.1.7",
        ],
    zip_safe=False,
)
