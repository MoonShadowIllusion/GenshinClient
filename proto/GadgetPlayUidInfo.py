# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GadgetPlayUidInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ProfilePicture import *


@dataclass
class GadgetPlayUidInfo(betterproto.Message):
    profile_picture: "ProfilePicture" = betterproto.message_field(2)
    battle_watcher_id: int = betterproto.uint32_field(6)
    uid: int = betterproto.uint32_field(7)
    icon: int = betterproto.uint32_field(14)
    score: int = betterproto.uint32_field(4)
    nickname: str = betterproto.string_field(3)
    online_id: str = betterproto.string_field(8)
