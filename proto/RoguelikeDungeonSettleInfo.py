# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RoguelikeDungeonSettleInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .RoguelikeSettleCoinInfo import *


@dataclass
class RoguelikeDungeonSettleInfo(betterproto.Message):
    stage_id: int = betterproto.uint32_field(5)
    is_final_level: bool = betterproto.bool_field(15)
    finished_challenge_cell_num_map: Dict[
        int, "RoguelikeSettleCoinInfo"
    ] = betterproto.map_field(3, betterproto.TYPE_UINT32, betterproto.TYPE_MESSAGE)
    is_coin_c_reach_limit: bool = betterproto.bool_field(13)
    cur_level: int = betterproto.uint32_field(9)
    total_coin_b_num: int = betterproto.uint32_field(6)
    total_coin_c_num: int = betterproto.uint32_field(10)