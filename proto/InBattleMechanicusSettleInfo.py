# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: InBattleMechanicusSettleInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .MultistageSettleWatcherInfo import *


@dataclass
class InBattleMechanicusSettleInfo(betterproto.Message):
    scene_time_ms: int = betterproto.uint64_field(15)
    total_token: int = betterproto.uint32_field(4)
    real_token: int = betterproto.uint32_field(8)
    watcher_list: List["MultistageSettleWatcherInfo"] = betterproto.message_field(7)
    is_success: bool = betterproto.bool_field(6)
    play_index: int = betterproto.uint32_field(3)
    difficulty_percentage: int = betterproto.uint32_field(10)
    group_id: int = betterproto.uint32_field(13)