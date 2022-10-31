# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TreasureMapActivityDetailInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .TreasureMapBonusChallengeInfo import *
from .TreasureMapRegionInfo import *


@dataclass
class TreasureMapActivityDetailInfo(betterproto.Message):
    active_region_index: int = betterproto.uint32_field(1)
    region_info_list: List["TreasureMapRegionInfo"] = betterproto.message_field(6)
    is_mp_challenge_touched: bool = betterproto.bool_field(7)
    treasure_close_time: int = betterproto.uint32_field(10)
    bonus_challenge_list: List[
        "TreasureMapBonusChallengeInfo"
    ] = betterproto.message_field(5)
    currency_num: int = betterproto.uint32_field(2)
    preview_reward_id: int = betterproto.uint32_field(14)
    min_open_player_level: int = betterproto.uint32_field(8)
    total_mp_spot_num: int = betterproto.uint32_field(13)
