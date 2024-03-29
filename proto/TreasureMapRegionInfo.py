# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TreasureMapRegionInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class TreasureMapRegionInfo(betterproto.Message):
    start_time: int = betterproto.uint32_field(6)
    current_progress: int = betterproto.uint32_field(11)
    is_done_mp_spot: bool = betterproto.bool_field(3)
    scene_id: int = betterproto.uint32_field(2)
    goal_points: int = betterproto.uint32_field(12)
    is_find_mp_spot: bool = betterproto.bool_field(4)
    region_radius: int = betterproto.uint32_field(1)
    region_center_pos: "Vector" = betterproto.message_field(9)
    region_id: int = betterproto.uint32_field(5)
