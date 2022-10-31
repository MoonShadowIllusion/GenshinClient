import requests

from crypto.BASE64 import b64Decode
from proto.QueryRegionListHttpRsp import QueryRegionListHttpRsp


def getQueryRegionList() -> QueryRegionListHttpRsp:
    url = 'https://dispatchcnglobal.yuanshen.com/query_region_list'
    params = {
        "version": "CNRELWin3.1.0",
        "lang": "2",
        "platform": "3",
        "binary": "1",
        "time": "359",
        "channel_id": "1",
        "sub_channel_id": "1"
    }
    _ = b64Decode(requests.get(url, params=params).text)
    """
    client_custom_config_encrypted 可通过 client_secret_key xor解密
    """

    return QueryRegionListHttpRsp.FromString(_)
