# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MechanicusUnlockGearRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MechanicusUnlockGearRsp(betterproto.Message):
    """
    CmdId: 3990 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(3)
    mechanicus_id: int = betterproto.uint32_field(8)
    gear_id: int = betterproto.uint32_field(14)
