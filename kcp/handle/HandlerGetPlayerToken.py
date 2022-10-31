import struct
import threading
import time

import Global
from crypto import RSADecrypt, MT19937_64, xor, b64Decode
from crypto.keys import OSCN, PACKET_XOR_KEY
from proto import GetPlayerTokenRsp, PlayerLoginReq, TrackingIOInfo, PingReq,AdjustTrackingInfo,PacketHead
from .BaseHandle import BaseHandle
from kcp.py_kcp import py_kcp
from kcp.Packet import Packet


class HandlerGetPlayerToken(BaseHandle):
    @staticmethod
    def func1(kcp: py_kcp, _: GetPlayerTokenRsp):
        """建立连接

        :param kcp: 套接字
        :param _: 数据
        :return: None
        """
        print(_)

        server_seed = RSADecrypt(b64Decode(_.encrypted_seed), OSCN)
        seed = xor(server_seed, Global.CLIENT_SEED)
        seed = int.from_bytes(seed, 'big', signed=False)
        new_xor_key = MT19937_64.MT64Generator(seed)
        Global.set_value(PACKET_XOR_KEY, new_xor_key)
        print(f'新xor密钥: {new_xor_key[:4].hex()}')
        # 收到后立马发送心跳
        def start_ping():
            print("开始发送心跳包")
            _ue_time = 10
            _client_time = int(time.time())
            while True:
                _now = int(time.time())
                _ue_time += _now - _client_time
                _client_time = _now
                ping_body = PingReq(
                    client_time=_client_time,
                    ue_time=_ue_time,
                    total_tick_time=5896
                )
                _head=Packet.make_head()
                _head.enet_is_reliable=0
                kcp.send_data(Packet.pack(_head, ping_body))
                time.sleep(10)

        threading.Thread(target=start_ping,name="心跳包").start()

        body = PlayerLoginReq(
            account_type=1,
            adjust_tracking_info=AdjustTrackingInfo(),
            device_info='operatingSystem:Windows 10  (10.0.0) 64bit&deviceModel:BOHL-WXX9 (HUAWEI)&graphicsDeviceName:AMD Radeon(TM) Graphics&graphicsDeviceType:Direct3D11&graphicsDeviceVendor:ATI&graphicsDeviceVersion:Direct3D 11.0 [level 11.1]&graphicsMemorySize:4431&processorCount:8&processorFrequency:1996&processorType:AMD Ryzen 7 4700U with Radeon Graphics &systemMemorySize:15741',
            device_uuid='7a3ea24ed3f172dc882af6721541a5173399a5fc1655361916696',
            language_type=2,
            device_name='DESKTOP-A58E2MI',
            system_version='Windows 10  (10.0.0) 64bit',
            client_version='CNRELWin3.1.0_R10916590_S10805493_D10941477',
            platform_type=3,
            token=_.token,
            sub_channel_id=1,
            client_data_version=10941477,
            unk2700__n_g_k_c_n_p_k_k_i_k_b='cf6e9b532d2ec49fb403d9a55b303b12',
            checksum_client_version='CNRELWin3.1.0',
            checksum='64309cf5f6d6b7c427d3e15622636372f9402b0a1cf311777c0d7b1ff7e6ac6624',
            tracking_io_info=TrackingIOInfo(
                client_tz='+8',
                rydevicetype='BOHL-WXX9 (HUAWEI)',
            ),
            client_verison_hash='0yHUWjWuiv+lxjrWmC4VPOfXe3s=',
            security_cmd_reply=bytes.fromhex('fd935ad5b1d0338e9e64f164c4dbfd3f360421da83c4c938c1f212f0db079c82'),
        )

        head = Packet.make_head()
        print(body)
        """
        GetPlayerToken中的security_cmd
        """
        o = open(r'C:\Users\xuke\Desktop\proto\PlayerLoginReq__1666978152487.bin','rb').read()
        body = PlayerLoginReq.FromString(o)
        kcp.send_data(Packet.pack(head, body))
        time.sleep(0.1)

    @staticmethod
    def getHandles() -> tuple[type, tuple]:
        return GetPlayerTokenRsp, (
            HandlerGetPlayerToken.func1,
        )
