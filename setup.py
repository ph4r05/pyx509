from distutils.core import setup

setup(
    name='pyx509',
    version='0.1.2',
    packages=['x509','x509.pkcs7','x509.pkcs7.asn1_models',],
    license='GNU Library General Public License',
    long_description=open('README').read(),
    install_requires=[
            "pyasn1 >= 0.1.7",
        ],
)