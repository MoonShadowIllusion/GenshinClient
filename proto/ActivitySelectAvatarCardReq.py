# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ActivitySelectAvatarCardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ActivitySelectAvatarCardReq(betterproto.Message):
    """
    CmdId: 2028 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    activity_id: int = betterproto.uint32_field(15)
    reward_id: int = betterproto.uint32_field(10)
