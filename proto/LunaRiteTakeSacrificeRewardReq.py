# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: LunaRiteTakeSacrificeRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class LunaRiteTakeSacrificeRewardReq(betterproto.Message):
    """
    CmdId: 8045 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    area_id: int = betterproto.uint32_field(11)
    index: int = betterproto.uint32_field(3)
