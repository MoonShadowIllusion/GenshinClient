import ec2b


def EC2BDecode(data: bytes) -> bytes:
    return ec2b.derive(data)
