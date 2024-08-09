#!/usr/local/bin/python

import pyotp
import time
import sys

try:
  base32_QRcode_secret = (sys.argv[1])

  totp_passcode = pyotp.TOTP(base32_QRcode_secret)
  print(totp_passcode.now())
except:
  print (f"example: {sys.argv[0]} <base32_QRcode> ")
  print (f"example: {sys.argv[0]} KZY4IBAHSPVP6YEWM2JFHPQ2AYCELUAJ")
  



"""
# NOTE: You dont need a 32-character length thats not a requirement. You just need the QR Code Secret however long it is in base32 form
# A helper function is provided to generate a 32-character base32 secret, compatible with Google Authenticator and other OTP apps
#random_characters_in_base32 = (pyotp.random_base32())

# Print 32-character base32 secret
#print(f"{random_characters_in_base32}")

"""


