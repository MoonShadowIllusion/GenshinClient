# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeAvatarRewardEventGetRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class HomeAvatarRewardEventGetRsp(betterproto.Message):
    """
    CmdId: 4833 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    item_list: List["ItemParam"] = betterproto.message_field(4)
    retcode: int = betterproto.int32_field(14)
    event_id: int = betterproto.uint32_field(8)