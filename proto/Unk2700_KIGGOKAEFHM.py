# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_KIGGOKAEFHM.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *
from .ProfilePicture import *


@dataclass
class Unk2700_KIGGOKAEFHM(betterproto.Message):
    item_list: List["ItemParam"] = betterproto.message_field(2)
    uid: int = betterproto.uint32_field(8)
    profile_picture: "ProfilePicture" = betterproto.message_field(1)
    nickname: str = betterproto.string_field(12)
