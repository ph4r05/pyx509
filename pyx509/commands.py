#*    pyx509 - Python library for parsing X.509
#*    Copyright (C) 2009-2012  CZ.NIC, z.s.p.o. (http://www.nic.cz)
#*
#*    This library is free software; you can redistribute it and/or
#*    modify it under the terms of the GNU Library General Public
#*    License as published by the Free Software Foundation; either
#*    version 2 of the License, or (at your option) any later version.
#*
#*    This library is distributed in the hope that it will be useful,
#*    but WITHOUT ANY WARRANTY; without even the implied warranty of
#*    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#*    Library General Public License for more details.
#*
#*    You should have received a copy of the GNU Library General Public
#*    License along with this library; if not, write to the
#*    Free Foundation, Inc., 51 Franklin Street, Fifth Floor,
#*    Boston, MA 02110-1301 USA
#*

import sys
from models import PKCS7
from models import X509Certificate


def print_certificate_info(derData):
    """
    Print certificate to stdout
    """
    X509Certificate.from_der(derData).display()


def print_certificate_info_cmd():
    """
    Print certificate command
    """
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: %s <certicate file>" % sys.argv[0]
        sys.exit(1)
    print_certificate_info(file(sys.argv[1]).read())


def print_signature_info(derData):
    """
    Print signature certificates to stdout
    """
    PKCS7.from_der(derData).display()


def print_signature_info_cmd():
    """
    Print signature certificates command
    """
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: %s <pkcs 7 signature file>" % sys.argv[0]
        sys.exit(1)
    print_signature_info(file(sys.argv[1]).read())


def print_timestamp_info(derData):
    """
    Print timestamp info
    """
    pkcs7 = PKCS7.from_der(derData)
    signedDate, valid_from, valid_to, signer = pkcs7.get_timestamp_info()
    print "Signature date: %s" % signedDate
    print "Signers certicate valid from: %s, to: %s" % (valid_from, valid_to)
    print "Signers certicate sbject: %s" % signer


def print_timestamp_info_cmd():
    """
    Print timestamp data
    """
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: %s <pkcs 7 signature file>" % sys.argv[0]
        sys.exit(1)
    print_timestamp_info(file(sys.argv[1]).read())
