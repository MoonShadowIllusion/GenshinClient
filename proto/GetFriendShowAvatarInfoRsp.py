# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetFriendShowAvatarInfoRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ShowAvatarInfo import *


@dataclass
class GetFriendShowAvatarInfoRsp(betterproto.Message):
    """
    CmdId: 4017 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    uid: int = betterproto.uint32_field(6)
    retcode: int = betterproto.int32_field(3)
    show_avatar_info_list: List["ShowAvatarInfo"] = betterproto.message_field(9)