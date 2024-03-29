# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayBattleInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ScenePlayBattleInfo(betterproto.Message):
    mode: int = betterproto.uint32_field(4)
    progress_stage_list: List[int] = betterproto.uint32_field(3)
    start_time: int = betterproto.uint32_field(10)
    duration: int = betterproto.uint32_field(14)
    play_type: int = betterproto.uint32_field(12)
    play_id: int = betterproto.uint32_field(1)
    prepare_end_time: int = betterproto.uint32_field(7)
    progress: int = betterproto.uint32_field(11)
    state: int = betterproto.uint32_field(8)
    type: int = betterproto.uint32_field(9)
