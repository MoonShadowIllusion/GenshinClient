# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TakeOfferingLevelRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TakeOfferingLevelRewardReq(betterproto.Message):
    """
    CmdId: 2919 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    level: int = betterproto.uint32_field(6)
    offering_id: int = betterproto.uint32_field(11)
