# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarExpeditionCallBackReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class AvatarExpeditionCallBackReq(betterproto.Message):
    """
    CmdId: 1752 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_guid: List[int] = betterproto.uint64_field(13)