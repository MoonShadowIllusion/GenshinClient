# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarDelNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class AvatarDelNotify(betterproto.Message):
    """
    CmdId: 1773 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_guid_list: List[int] = betterproto.uint64_field(13)