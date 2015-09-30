__author__ = 'Red_C0der'



def newkey():
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    return key


def encrypt(key, string):
    from cryptography.fernet import Fernet
    f = Fernet(key)
    token = f.encrypt(string)
    return token


def decrypt(key, token):
    from cryptography.fernet import Fernet
    f = Fernet(key)
    return f.decrypt(token)
