import requests

from .BaseLogin import LoginInterface
from crypto import RSAEncrypt, b64Encode
from crypto.keys import LOGIN


class LoginByAccount(LoginInterface):
    __header = {
        "User-Agent": "UnityPlayer/2017.4.30f1 (UnityWebRequest/1.0, libcurl/7.51.0-DEV)",
        "Accept-Encoding": "identity",
        "Content-Type": "application/json",
        "x-rpc-client_type": "3",
        "x-rpc-sys_version": "Windows%2010%20%20%2810.0.0%29%2064bit",
        "x-rpc-device_id": "7a3ea24ed3f172dc882af6721541a5173399a5fc1655361916696",
        "x-rpc-device_model": "BOHL-WXX9%20%28HUAWEI%29",
        "x-rpc-device_name": "DESKTOP-A58E2MI",
        "x-rpc-mdk_version": "2.3.1.2",
        "x-rpc-channel_version": "2.3.1.2",
        "x-rpc-channel_id": "1",
        "x-rpc-sub_channel_id": "1",
        "x-rpc-language": "zh-cn",
        "x-rpc-game_biz": "hk4e_cn",
        "x-rpc-device_fp": "38d7eac08c64b",
        "X-Unity-Version": "2017.4.30f1"
    }

    def __init__(self, account: str, password: str):
        super().__init__(account)
        self.__password = password

    def __check(self) -> str:
        url = 'https://gameapi-account.mihoyo.com/account/risky/api/check?'
        data = {
            "action_type": "login",
            "api_name": "/shield/api/login",
            "username": self.account
        }
        _ = requests.post(url, json=data, headers=self.__header).json()
        data_id = _["data"]["id"]
        return data_id

    def getToken(self) -> str:
        data_id = self.__check()
        url = 'https://hk4e-sdk.mihoyo.com/hk4e_cn/mdk/shield/api/login'
        data = {
            "account": self.account,
            "password": b64Encode(RSAEncrypt(self.__password.encode(), LOGIN)),
            "is_crypto": True
        }
        header = self.__header.copy()
        header.update({"x-rpc-risky": f"id={data_id};c=;s=;v="})
        _ = requests.post(url, json=data, headers=header).json()
        return _["data"]["account"]["token"]
