# -*- coding: utf-8 -*-

import sys
import unittest
import base64
from pyasn1.type import tag, namedtype, namedval, univ, char, useful
from pyasn1.codec.der.decoder import decode

test = '0C414D696E6973746572696F206465206C6120506F6CC3AD74696361205465727269746F7269616C2079' \
       '2041646D696E69737472616369C3B36E2050C3BA626C696361'
testb = base64.b16decode(test)
expected = u'Ministerio de la Política Territorial y Administración Pública'


class SimpleTest(unittest.TestCase):
    def test_utf8(self):
        utfbin = testb[2:]
        self.assertEqual(utfbin.decode('utf-8'), expected)

    def test_decode(self):
        asn1 = decode(testb, asn1Spec=char.UTF8String())
        res = asn1[0]

        print('Decoded type: %s, value: \n\t%s' % (type(res), str(res)))

        # this works in the broken version:
        # print('Decoded type: %s, value iso-8859-1 decoded: \n\t%s' % (type(res), str(res).decode('iso-8859-1')))

        if sys.version_info[0] <= 2:
            self.assertEqual(unicode(res), expected)
        self.assertEqual(str(res).decode('utf-8'), expected)


if __name__ == '__main__':
    unittest.main()
