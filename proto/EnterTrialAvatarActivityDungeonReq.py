# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EnterTrialAvatarActivityDungeonReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class EnterTrialAvatarActivityDungeonReq(betterproto.Message):
    """
    CmdId: 2118 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    enter_point_id: int = betterproto.uint32_field(10)
    trial_avatar_index_id: int = betterproto.uint32_field(5)
    activity_id: int = betterproto.uint32_field(14)
