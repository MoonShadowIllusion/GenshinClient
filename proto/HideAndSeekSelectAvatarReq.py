# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HideAndSeekSelectAvatarReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class HideAndSeekSelectAvatarReq(betterproto.Message):
    """
    CmdId: 5330 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_id: int = betterproto.uint32_field(8)
