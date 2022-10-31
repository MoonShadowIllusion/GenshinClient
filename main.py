import Global
from crypto import EC2BDecode, xor
from kcp import KCPClient
from server import getQueryCurRegion, getQueryRegionList
from crypto.keys import PACKET_XOR_KEY

Global.init()

if __name__ == "__main__":
    ls = getQueryRegionList()

    region = ls.region_list[0]

    cur = getQueryCurRegion(region)

    Global.set_value(PACKET_XOR_KEY, EC2BDecode(cur.client_secret_key))

    k=EC2BDecode(ls.client_secret_key)
    tp = xor(ls.client_custom_config_encrypted, k)
    print(tp.decode())
    # server = ('47.116.111.187', 22102)
    server = (cur.region_info.gateserver_ip, cur.region_info.gateserver_port)
    uid = '265084555'
    token = 'c8a5ef0289ce6963f7aa477b9717487de429fe5f'
    cli = KCPClient(uid, token, server)
