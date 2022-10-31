import requests

from crypto.keys import OSCN
from crypto import b64Decode, RSADecrypt
from proto.RegionSimpleInfo import RegionSimpleInfo
from proto.QueryCurrRegionHttpRsp import QueryCurrRegionHttpRsp


def getQueryCurRegion(region: RegionSimpleInfo) -> QueryCurrRegionHttpRsp:
    url = region.dispatch_url
    params = {
        "version": "CNRELWin3.1.0",
        "lang": "2",
        "platform": "3",
        "binary": "1",
        "time": "359",
        "channel_id": "1",
        "sub_channel_id": "1",
        "account_type": "1",
        "dispatchSeed": "70da6fe57b6b37e0",
        "key_id": "2"
    }
    _ = requests.get(url, params=params).json()
    content = b64Decode(_["content"])
    content = RSADecrypt(content, OSCN)
    return QueryCurrRegionHttpRsp.FromString(content)
