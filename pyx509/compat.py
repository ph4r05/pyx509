# some compatibility functions

from models import PKCS7


def get_time_stamp_info(derData):
    return PKCS7.from_der(derData).get_timestamp_info()
