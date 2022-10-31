import select
import threading
import time
from socket import socket
from .py_kcp import py_kcp
from struct import unpack, pack
from .Packet import Packet
from .handle import handles


class KCPClientListening:
    def __init__(self, remote_addr: tuple[str, int]):
        self.remote_addr = remote_addr
        self.conv1 = 0
        self.conv2 = 0

    def onConnect(self, _udp: socket) -> tuple[int, int]:
        """第一次连接，发送握手包获取会话编号

        :param _udp: udp 套接字
        :return: conv1, conv2 直接使用，不需要转换
        """

        def first_recv():
            while True:
                _data, _remote_addr = _udp.recvfrom(2048)
                if _remote_addr == self.remote_addr:
                    self.conv1, self.conv2 = unpack('>xxxxIIxxxxxxxx', _data)
                    break

        t = threading.Thread(target=first_recv)
        t.start()
        hand_packet = bytes.fromhex('000000ff0000000000000000499602d2ffffffff')

        print("请求token")
        _udp.sendto(hand_packet, self.remote_addr)
        t.join()
        return self.conv1, self.conv2

    def onMessage(self, _kcp: py_kcp, _data: bytes) -> None:
        """收到消息

        :param _kcp: kcp套接字
        :param _data: 收到的数据
        """

        head, body = Packet.unpack(_data)
        if head and body:
            print('支持的消息')
            [i(_kcp, body) for i in handles[type(body)]]
        else:
            print('不支持的消息')

    def onDisconnect(self, _kcp: py_kcp) -> None:
        """断开连接

        :return:
        """
        pass

    def onException(self):
        pass

