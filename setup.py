from distutils.core import setup
from setuptools import find_packages

setup(
    name='pyx509_ph4',
    version='0.1.6',
    packages=find_packages(),
    url='https://deadcode.me',
    license='LICENSE.txt',
    description='Parse x509v3 certificates and PKCS7 signatures',
    long_description=open('README.rst').read(),
    install_requires=[
            "pyasn1 >= 0.1.7",
    ],
    entry_points={
        'console_scripts': [
            'x509_parse.py = pyx509.commands:print_certificate_info_cmd',
            'pkcs7_parse.py = pyx509.commands:print_signature_info_cmd',
        ]
    },
    test_suite='pyx509.test',
    zip_safe=False,
)
