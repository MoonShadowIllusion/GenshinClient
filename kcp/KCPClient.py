import errno
import threading
import time
from socket import socket, AF_INET, SOCK_DGRAM, error, SOL_SOCKET, SO_REUSEADDR

import Global
from crypto import b64Encode, RSAEncrypt
from crypto.keys import SIGNATURE
from proto import GetPlayerTokenReq
from .KCPClientListener import KCPClientListening
from .Packet import Packet
from .py_kcp import py_kcp


def recv_from_udp(_udp: socket, kcp_sock: py_kcp, remote_addr: tuple[str, int]):
    while True:
        _data, _addr = _udp.recvfrom(4096)
        if _addr == remote_addr:
            kcp_sock.input_data(_data)


def recv_kcp(kcp_sock: py_kcp, listener: KCPClientListening):
    try:
        while True:
            data = kcp_sock.recv_data()
            if data:
                listener.onMessage(kcp_sock, data)
            time.sleep(0.5)
    except error as arg:
        eno, msg = arg
        if eno != errno.EAGAIN and eno != errno.EINTR:
            pass
    return None


def send_fun(_udp: socket, data: bytes):
    _udp.send(data)


def flush_kcp(kcp_sock: py_kcp):
    sleep_time_f = 0.01

    while True:
        time.sleep(sleep_time_f)
        kcp_sock.update(int(time.time()))
    pass


class KCPClient:
    def __init__(self, account_uid: str, combo_token: str, _remote_addr: tuple[str, int]):
        self.__remote_addr = _remote_addr

        udp_sock = socket(AF_INET, SOCK_DGRAM)
        udp_sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        # udp_sock.setblocking(False)
        udp_sock.connect(self.__remote_addr)

        self.listener = KCPClientListening(self.__remote_addr)

        conv1, conv2 = self.listener.onConnect(udp_sock)
        # 设置kcp
        self.kcp_sock = py_kcp(conv1, conv2, udp_sock, send_fun)
        self.kcp_sock.set_nodelay(1, 10, 2, 1)
        self.kcp_sock.win_size(10, 128)
        self.kcp_sock.mtu_size(576)

        threading.Thread(target=recv_from_udp, args=(udp_sock, self.kcp_sock, self.__remote_addr)).start()
        threading.Thread(target=recv_kcp, args=(self.kcp_sock, self.listener)).start()
        threading.Thread(target=flush_kcp, args=(self.kcp_sock,)).start()

        #

        head = Packet.make_head()
        body = GetPlayerTokenReq(
            account_token=combo_token,
            account_uid=account_uid,
            client_seed=b64Encode(RSAEncrypt(Global.CLIENT_SEED, SIGNATURE)),
            channel_id=1,
            account_type=1,
            sub_channel_id=1,
            key_id=2,
            platform_type=3
        )
        pack = Packet.pack(head, body)
        self.kcp_sock.send_data(pack)
        # self.kcp_sock.update(GetMillisecond())
        # TODO kcp 套接字设置
