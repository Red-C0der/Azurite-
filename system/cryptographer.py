__author__ = 'Red_C0der'



def newkey():
    import os
    BLOCK_SIZE = 32
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    secret = os.urandom(BLOCK_SIZE)
    return secret


def encrypt(key, string):
    from Crypto.Cipher import AES
    import base64
    BLOCK_SIZE = 32
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))
    cipher = AES.new(key)
    encoded = EncodeAES(cipher, string)
    return encoded


def decrypt(key, token):
    from Crypto.Cipher import AES
    import base64
    BLOCK_SIZE = 32
    PADDING = '{'
    pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING
    DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)
    cipher = AES.new(key)
    decoded = DecodeAES(cipher, token)
    return decoded
