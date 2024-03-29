# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeModuleComfortInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class HomeModuleComfortInfo(betterproto.Message):
    module_id: int = betterproto.uint32_field(13)
    room_scene_comfort_value: int = betterproto.uint32_field(9)
    world_scene_block_comfort_value_list: List[int] = betterproto.uint32_field(3)
