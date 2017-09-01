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
TEST_SIGNATURE = join(TEST_DATA_DIR, 'test_signature.der')
TEST_SIGNATURE_3 = join(TEST_DATA_DIR, 'test_sig3.der')
TEST_SIGNATURE_3_TXT = join(TEST_DATA_DIR, 'test_sig3.txt')
TEST_SIGNATURE_4 = join(TEST_DATA_DIR, 'test_sig4.der')
TEST_SIGNATURE_4_TXT = join(TEST_DATA_DIR, 'test_sig4.txt')
TEST_SIGNATURE_TXT = join(TEST_DATA_DIR, 'test_signature.txt')
TEST_TIMESTAMP = join(TEST_DATA_DIR, 'test_timestamp.der')
TEST_TIMESTAMP_TXT = join(TEST_DATA_DIR, 'test_timestamp.txt')
TEST_TIMESTAMP_INFO_TXT = join(TEST_DATA_DIR, 'test_timestamp_info.txt')


class SimpleTest(unittest.TestCase):

    def setUp(self):
        sys.stdout = BytesIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_certificate(self):
        self.maxDiff = None
        commands.print_certificate_info(open(TEST_CERTIFICATE, 'rb').read())
        txt1 = u'%s' % sys.stdout.getvalue()
        txt2 = open(TEST_CERTIFICATE_TXT).read()
        self.assertEqual(txt1, txt2)

    def test_signature(self):
        commands.print_signature_info(open(TEST_SIGNATURE, 'rb').read())
        txt1 = u'%s' % sys.stdout.getvalue()
        txt2 = open(TEST_SIGNATURE_TXT).read()
        self.assertEqual(txt1, txt2)

    def test_timestamp(self):
        # import sys
        # sys.stdout = sys.__stdout__
        commands.print_signature_info(open(TEST_TIMESTAMP, 'rb').read())

        self.maxDiff = None
        txt1 = sys.stdout.getvalue().decode('utf8')
        txt2 = open(TEST_TIMESTAMP_TXT, 'rU', encoding='utf8').read()

        # TODO: fix unicode
        # pyasn1: char.py - the ._value is already broken unicode.
        # UTF8String initialized, using prettyIn(), calling unicode on the input value
        # which is OctetString, containing string encoded input, in encoding iso-8859-1
        #
        # unicode(x) call on the OctetString causes .decode('iso-8859-1') call which breaks
        # the encoding.
        # https://github.com/etingof/pyasn1/issues/65
        #

        # with open('/tmp/b1', 'w') as fh:
        #     fh.write(txt1)
        # with open('/tmp/b2', 'w') as fh:
        #     fh.write(txt2)
        self.assertEqual(txt1, txt2)

    def test_timestamp_info(self):
        commands.print_timestamp_info(open(TEST_TIMESTAMP, 'rb').read())
        txt1 = u'%s' % sys.stdout.getvalue()
        txt2 = open(TEST_TIMESTAMP_INFO_TXT).read()
        self.assertEqual(txt1, txt2)

    def test_signature_3(self):
        self.der_test(TEST_SIGNATURE_3, TEST_SIGNATURE_3_TXT)

    def test_signature_4(self):
        self.der_test(TEST_SIGNATURE_4, TEST_SIGNATURE_4_TXT)

    def der_test(self, fname, exam):
        p7 = PKCS7.from_der(open(fname, 'rb').read())
        self.sub_test(p7)
        txt1 = sys.stdout.getvalue().decode('utf8')
        txt2 = open(exam, 'rU', encoding='utf8').read()
        self.assertEqual(txt1, txt2)

    def sub_test(self, p7):
        signed_date, valid_from, valid_to, signer = p7.get_timestamp_info()
        print('Sign date: %s' % signed_date)
        print('Sign not before: %s' % valid_from)
        print('Sign not after: %s' % valid_to)
        print('Signer: %s' % str(signer))
        if len(p7.content.signerInfos) > 0:
            signer_info = p7.content.signerInfos[0]
            print('Signer serial: %s' % signer_info.serial_number)
            print('Sign issuer: %s' % signer_info.issuer)
            print('Sign algorithm: %s' % signer_info.oid2name(signer_info.digest_algorithm))


if __name__ == '__main__':
    unittest.main()
