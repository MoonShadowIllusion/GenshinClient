from itertools import cycle


def xor(data: bytes, key: bytes) -> bytes:
    return bytes(v ^ k for (v, k) in zip(data, cycle(key)))
