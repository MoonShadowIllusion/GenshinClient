# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SetPlayerBornDataReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SetPlayerBornDataReq(betterproto.Message):
    """
    CmdId: 105 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_id: int = betterproto.uint32_field(2)
    nick_name: str = betterproto.string_field(13)