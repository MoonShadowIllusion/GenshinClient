# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CrucibleBattleUidInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ProfilePicture import *


@dataclass
class CrucibleBattleUidInfo(betterproto.Message):
    profile_picture: "ProfilePicture" = betterproto.message_field(15)
    uid: int = betterproto.uint32_field(4)
    nickname: str = betterproto.string_field(5)
    online_id: str = betterproto.string_field(13)
    icon: int = betterproto.uint32_field(11)
