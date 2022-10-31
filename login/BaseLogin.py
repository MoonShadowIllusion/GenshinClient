import hashlib
import hmac
import json
from abc import abstractmethod, ABCMeta

import requests

import Global
from crypto import b64Encode


class LoginInterface(object):
    def __init__(self, account: str):
        self.account = account

    def getToken(self) -> str:
        raise NotImplementedError("未实现")

    def getComboToken(self) -> str:
        # print(dir(self))
        token = self.getToken()
        _data = {"uid": self.account, "guest": False, "token": token}
        url = 'https://hk4e-sdk.mihoyo.com/hk4e_cn/combo/granter/login/v2/login?'
        data = {
            "data": json.dumps(_data),
            "app_id": 4,
            "channel_id": 1,
            "device": Global.DEVICE,
        }
        data_keys_sorted = sorted(data.keys())
        _ = '&'.join([f'{i}={data[i]}' for i in data_keys_sorted])
        key = "d0d3a7342df2026a70f650b907800111"
        data["sign"] = b64Encode(hmac.new(key.encode(), _.encode(), digestmod=hashlib.sha256).digest())

        _ = requests.post(url, json=data).json()
        return _["data"]["combo_token"]
