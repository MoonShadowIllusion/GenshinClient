# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerOfferingData.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class PlayerOfferingData(betterproto.Message):
    offering_id: int = betterproto.uint32_field(1)
    is_first_interact: bool = betterproto.bool_field(15)
    level: int = betterproto.uint32_field(12)
    taken_level_reward_list: List[int] = betterproto.uint32_field(8)
    is_new_max_level: bool = betterproto.bool_field(6)
