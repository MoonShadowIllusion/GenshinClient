# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RedeemLegendaryKeyRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RedeemLegendaryKeyRsp(betterproto.Message):
    """
    CmdId: 441 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    legendary_key_count: int = betterproto.uint32_field(11)
    retcode: int = betterproto.int32_field(14)
