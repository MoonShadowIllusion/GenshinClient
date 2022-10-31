from Crypto.PublicKey import RSA
from os.path import dirname, join

__base_path = dirname(__file__)


def __getKeyFile(keyname: str):
    with open(join(__base_path, keyname), 'rb') as f:
        return f.read()


def __getRsaKey(keyname: str) -> RSA.RsaKey:
    return RSA.import_key(__getKeyFile(keyname))


OSCN = __getRsaKey("OSCN.pem")

LOGIN = __getRsaKey("LOGIN.pem")

SIGNATURE = __getRsaKey("SIGNATURE.pem")

# 加密数据包
PACKET_XOR_KEY = "PACKET_XOR_KEY"
