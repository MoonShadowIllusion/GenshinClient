# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TakePlayerLevelRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TakePlayerLevelRewardReq(betterproto.Message):
    """
    CmdId: 129 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    level: int = betterproto.uint32_field(3)
