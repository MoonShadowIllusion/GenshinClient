# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChannelerSlabLoopDungeonTakeScoreRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ChannelerSlabLoopDungeonTakeScoreRewardReq(betterproto.Message):
    """
    CmdId: 8684 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    reward_index: int = betterproto.uint32_field(8)
