# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetRecentMpPlayerListRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .FriendBrief import *


@dataclass
class GetRecentMpPlayerListRsp(betterproto.Message):
    """
    CmdId: 4050 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(13)
    recent_mp_player_brief_list: List["FriendBrief"] = betterproto.message_field(14)
