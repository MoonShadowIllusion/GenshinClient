# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TakeCoopRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TakeCoopRewardReq(betterproto.Message):
    """
    CmdId: 1973 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    reward_config_id: int = betterproto.uint32_field(6)
