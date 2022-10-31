# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlantFlowerFriendFlowerWishData.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .ProfilePicture import *


@dataclass
class PlantFlowerFriendFlowerWishData(betterproto.Message):
    profile_picture: "ProfilePicture" = betterproto.message_field(3)
    uid: int = betterproto.uint32_field(5)
    nickname: str = betterproto.string_field(14)
    flower_num_map: Dict[int, int] = betterproto.map_field(
        12, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )