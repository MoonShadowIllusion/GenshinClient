# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FishPoolInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class FishPoolInfo(betterproto.Message):
    pool_id: int = betterproto.uint32_field(1)
    fish_area_list: List[int] = betterproto.uint32_field(2)
    today_fish_num: int = betterproto.uint32_field(3)
