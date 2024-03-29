# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChannelerSlabLoopDungeonInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ChannelerSlabLoopDungeonInfo(betterproto.Message):
    score: int = betterproto.uint32_field(7)
    dungeon_index: int = betterproto.uint32_field(4)
    open_time: int = betterproto.uint32_field(12)
    is_first_pass_reward_taken: bool = betterproto.bool_field(9)
    last_condition_id_list: List[int] = betterproto.uint32_field(14)
    is_open: bool = betterproto.bool_field(1)
