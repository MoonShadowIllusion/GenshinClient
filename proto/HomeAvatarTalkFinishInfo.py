# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeAvatarTalkFinishInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class HomeAvatarTalkFinishInfo(betterproto.Message):
    avatar_id: int = betterproto.uint32_field(9)
    finish_talk_id_list: List[int] = betterproto.uint32_field(3)