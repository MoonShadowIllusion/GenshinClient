# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeAvatarTalkReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class HomeAvatarTalkReq(betterproto.Message):
    """
    CmdId: 4688 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    talk_id: int = betterproto.uint32_field(12)
    avatar_id: int = betterproto.uint32_field(15)