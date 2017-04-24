import pyotp
import time


def otp_gen():

    totp = pyotp.TOTP('base32secret3232')
    otp = totp.now()
    return otp


def otp_ver(otp):
    p = int(otp)
    t = pyotp.TOTP('base32secret3232')
    return t.verify(p)
