# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarExpeditionGetRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AvatarExpeditionGetRewardReq(betterproto.Message):
    """
    CmdId: 1623 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_guid: int = betterproto.uint64_field(14)
