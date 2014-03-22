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
    Print certificate
    """
    X509Certificate.from_der(derData).display()


def print_certificate_info_cmd():
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: %s <certicate file>" % sys.argv[0]
        sys.exit(1)
    print_certificate_info(file(sys.argv[1]).read())


def print_signature_info(derData):
    """
    Print certificates of signature
    """
    PKCS7.from_der(derData).display()


def print_signature_info_cmd():
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: %s <pkcs 7 signature file>" % sys.argv[0]
        sys.exit(1)
    print_signature_info(file(sys.argv[1]).read())
