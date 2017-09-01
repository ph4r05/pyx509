# -*- coding: utf-8 -*-
# *    pyx509 - Python library for parsing X.509
# *    Copyright (C) 2009-2012  CZ.NIC, z.s.p.o. (http://www.nic.cz)
# *
# *    This library is free software; you can redistribute it and/or
# *    modify it under the terms of the GNU Library General Public
# *    License as published by the Free Software Foundation; either
# *    version 2 of the License, or (at your option) any later version.
# *
# *    This library is distributed in the hope that it will be useful,
# *    but WITHOUT ANY WARRANTY; without even the implied warranty of
# *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# *    Library General Public License for more details.
# *
# *    You should have received a copy of the
# *    GNU Library General Public License along with this library;
# *    if not, write to the Free Foundation, Inc.,
# *    51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
# *

from builtins import str as text

import os
from io import open
from os.path import join
from io import BytesIO
import sys
import unittest

from pyx509 import commands
from pyx509.models import PKCS7, PKCS7_SignedData

TEST_DATA_DIR = join(os.path.dirname(__file__), 'data')
TEST_CERTIFICATE = join(TEST_DATA_DIR, 'test_certificate.der')
TEST_CERTIFICATE_TXT = join(TEST_DATA_DIR, 'test_certificate.txt')


class SimpleTest(unittest.TestCase):

    def setUp(self):
        sys.stdout = BytesIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_certificate(self):
        self.maxDiff = None
        # sys.stdout = sys.__stdout__
        commands.print_certificate_info(open(TEST_CERTIFICATE, 'rb').read())

        # Certificate policy extension is not processed as it contains VisibleString which is not decodeable
        # in the us-ascii encoding (VisibleString def).
        txt1 = u'%s' % sys.stdout.getvalue()
        txt2 = open(TEST_CERTIFICATE_TXT).read()
        self.assertEqual(txt1, txt2)


if __name__ == '__main__':
    unittest.main()
