
#*    pyx509 - Python library for parsing X.509
#*    Copyright (C) 2009-2010  CZ.NIC, z.s.p.o. (http://www.nic.cz)
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
#*    License along with this library; if not, write to the Free
#*    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#*

# standard library imports
import base64
import hashlib
import logging
logger = logging.getLogger("pkcs7.digest")

RSA_NAME = "RSA"


class LazyB64:
    '''
    Lazy base 64 converter for logging.
    '''

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return base64.b64encode(self.data)


def calculate_digest(data, alg):
    '''
    Calculates digest according to algorithm
    '''
    try:
        alg = alg.replace('-', '')
        digest = hashlib.new(alg, data).digest()
        logger.debug("Calculated hash from input data: %s", LazyB64(digest))
        return digest
    except ValueError:
        logger.error("Unknown digest algorithm : %s", alg)
        raise
