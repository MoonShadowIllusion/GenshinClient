import time
from typing import Any

from proto.PacketHead import PacketHead
from betterproto import Message
import struct
from proto import proto2id, id2proto
from crypto import xor
from crypto.keys import PACKET_XOR_KEY
import Global


class Packet:
    @staticmethod
    def pack(head: PacketHead, body: Message) -> bytes:
        cmd_id = proto2id.get(type(body), None)
        if cmd_id:
            head = head.SerializeToString()
            head_len = len(head)
            body = body.SerializeToString()
            body_len = len(body)
            fmt = f'!HHHI{head_len}s{body_len}sH'
            return xor(struct.pack(fmt, 0x4567, cmd_id, head_len, body_len, head, body, 0x89AB),
                       Global.get_value(PACKET_XOR_KEY))
        else:
            raise NotImplementedError(f'{type(body).__name__} 的 cmd_id 没有添加')

    @staticmethod
    def unpack(data: bytes) -> tuple[Message, Message] | tuple[None, None]:
        """只有 ```proto.id2proto```中被定义才会解包，否则返回None

        :param data:
        :return:
        """
        data = xor(data, Global.get_value(PACKET_XOR_KEY))

        head_len, = struct.unpack('!H', data[4:6])
        body_len, = struct.unpack('!I', data[6:10])
        fmt = f'!xxHHI{head_len}s{body_len}sxx'
        cmd_id, head_len, body_len, head, body = struct.unpack(fmt, data)
        tp = id2proto.get(cmd_id, None)

        return (PacketHead.FromString(head), tp.FromString(body)) if tp else (None, None)

    @staticmethod
    def make_head() -> PacketHead:
        """获取基础包"""
        return PacketHead(
            sent_ms=int(time.time() * 1000),
            client_sequence_id=Global.get_value(Global.client_sequence_id),
            enet_is_reliable=1
        )
