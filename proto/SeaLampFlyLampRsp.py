# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SeaLampFlyLampRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SeaLampFlyLampRsp(betterproto.Message):
    """
    CmdId: 2192 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    item_num: int = betterproto.uint32_field(9)
    item_id: int = betterproto.uint32_field(15)
    retcode: int = betterproto.int32_field(14)