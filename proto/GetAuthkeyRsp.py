# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetAuthkeyRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class GetAuthkeyRsp(betterproto.Message):
    """
    CmdId: 1473 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    auth_appid: str = betterproto.string_field(4)
    sign_type: int = betterproto.uint32_field(15)
    retcode: int = betterproto.int32_field(6)
    authkey_ver: int = betterproto.uint32_field(9)
    game_biz: str = betterproto.string_field(11)
    authkey: str = betterproto.string_field(3)