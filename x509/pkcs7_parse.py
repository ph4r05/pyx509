#!/usr/bin/env python
import sys
import base64
from pkcs7 import pkcs7_decoder
from x509_parse import print_certificate_details
from pkcs7_models import X509Certificate, SignerInfo
from pkcs7.asn1_models.oid import oid_map


def pkcs7_parse(derData):
    """Decodes certificate.
    @param derData: DER-encoded pkcs7
    @returns: PKCS7 structure (tree).
    """
    return pkcs7_decoder.decode_qts(derData)


def print_signature_info(derData):
    """
    Print certificates of signature
    """
    pkcs7 = pkcs7_parse(derData)
    typ, content = pkcs7
    version, digestAlgorithms, encapsulatedContentInfo, certificates, crls, signerInfos = content
    print "= PKCS7 signature block ="
    print "PKCS7 Version:", version
    for i, signerInfo in enumerate(signerInfos):
        print "== Signer info #%s ==" % i
        signerInfo = SignerInfo(signerInfo)
        print "Certificate serial number: 0x%x" % signerInfo.serial_number
        print "Issuer:", signerInfo.issuer
        print "Digest Algorithm:", oid_map.get(
            signerInfo.digest_algorithm, signerInfo.digest_algorithm)
        print "Signature (b64):"
        signature = base64.standard_b64encode(signerInfo.signature)
        while signature:
            print "    ", signature[:60]
            signature = signature[60:]
        if signerInfo.auth_attributes:
            print "Attributes:"
            for attr in signerInfo.auth_attributes.attributes:
                print  "    ", str(attr)
        print "== EOF Signer info #%s ==" % i
    for cert in certificates:
        print_certificate_details(X509Certificate(cert[0]))
    print "= EOF PKCS7 signature block ="


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print >> sys.stderr, "Usage: pkcs7_parse.py pkcs7_enveloped.der"
        sys.exit(1)
    der_file = sys.argv[1]
    print_signature_info(file(der_file).read())
