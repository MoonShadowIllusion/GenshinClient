# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TowerSurrenderRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TowerSurrenderRsp(betterproto.Message):
    """
    CmdId: 2465 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(9)
