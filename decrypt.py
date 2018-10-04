from Crypto.Cipher import AES
import base64
import os
import sys 
import getpass 
# the block size for the cipher object; must be 16, 24, or 32 for AES
BLOCK_SIZE = 32
 
# the character used for padding--with a block cipher such as AES, the value
# you encrypt must be a multiple of BLOCK_SIZE in length. This character is
# used to ensure that your value is always a multiple of BLOCK_SIZE
PADDING = '{'
 
DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)

temp = sys.argv[1] + "1234567890123456789012345678901234567890"
secret = temp[:32]

# create a cipher object using the random secret
cipher = AES.new(secret)
#print "This is the cipher " + cipher 
# encode a string
encoded = sys.argv[2]
 
# decode the encoded string
decoded = DecodeAES(cipher, encoded)
print 'Decrypted string:', decoded
