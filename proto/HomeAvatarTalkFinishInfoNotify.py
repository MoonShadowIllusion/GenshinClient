# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeAvatarTalkFinishInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .HomeAvatarTalkFinishInfo import *


@dataclass
class HomeAvatarTalkFinishInfoNotify(betterproto.Message):
    """
    CmdId: 4896 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_talk_info_list: List["HomeAvatarTalkFinishInfo"] = betterproto.message_field(
        9
    )
