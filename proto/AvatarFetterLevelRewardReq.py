# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarFetterLevelRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AvatarFetterLevelRewardReq(betterproto.Message):
    """
    CmdId: 1653 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_guid: int = betterproto.uint64_field(1)
    fetter_level: int = betterproto.uint32_field(6)