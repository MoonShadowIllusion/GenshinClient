# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerCookArgsRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PlayerCookArgsRsp(betterproto.Message):
    """
    CmdId: 168 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(4)
    qte_range_ratio: float = betterproto.float_field(12)
