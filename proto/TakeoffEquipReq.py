# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TakeoffEquipReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TakeoffEquipReq(betterproto.Message):
    """
    CmdId: 605 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_guid: int = betterproto.uint64_field(8)
    slot: int = betterproto.uint32_field(15)
