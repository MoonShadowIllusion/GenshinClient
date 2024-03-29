# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BounceConjuringGallerySettleInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto

from .ExhibitionDisplayInfo import *
from .OnlinePlayerInfo import *


@dataclass
class BounceConjuringGallerySettleInfo(betterproto.Message):
    player_info: "OnlinePlayerInfo" = betterproto.message_field(14)
    destroyed_machine_count: int = betterproto.uint32_field(5)
    fever_count: int = betterproto.uint32_field(6)
    normal_hit_count: int = betterproto.uint32_field(4)
    damage: float = betterproto.float_field(11)
    gadget_count_map: Dict[int, int] = betterproto.map_field(
        15, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    score: int = betterproto.uint32_field(12)
    perfect_hit_count: int = betterproto.uint32_field(8)
    card_list: List["ExhibitionDisplayInfo"] = betterproto.message_field(7)
