# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MechanicusLevelupGearRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MechanicusLevelupGearRsp(betterproto.Message):
    """
    CmdId: 3999 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    gear_id: int = betterproto.uint32_field(7)
    mechanicus_id: int = betterproto.uint32_field(2)
    after_gear_level: int = betterproto.uint32_field(12)
    retcode: int = betterproto.int32_field(8)
