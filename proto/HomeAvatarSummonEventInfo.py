# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeAvatarSummonEventInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class HomeAvatarSummonEventInfo(betterproto.Message):
    avatar_id: int = betterproto.uint32_field(3)
    guid: int = betterproto.uint32_field(8)
    event_id: int = betterproto.uint32_field(9)
    suit_id: int = betterproto.uint32_field(12)
    event_over_time: int = betterproto.uint32_field(2)
    random_position: int = betterproto.uint32_field(10)
