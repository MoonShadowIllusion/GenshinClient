from Crypto import Random
from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA


def RSAEncrypt(data: bytes, key: RSA.RsaKey):
    cipher = PKCS1_v1_5.new(key)
    return cipher.encrypt(data)


def RSADecrypt(data: bytes, key: RSA.RsaKey):
    cipher = PKCS1_v1_5.new(key)
    chunk_size = 256

    return b''.join(
        [cipher.decrypt(data[i:i + chunk_size], Random.new().read) for i in range(0, len(data), chunk_size)])
