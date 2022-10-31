from base64 import b64encode as be, b64decode as bd


def b64Encode(_input: bytes) -> str:
    return be(_input).decode()


def b64Decode(_input: str) -> bytes:
    return bd(_input)
