# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SummerTimeSprintBoatRecord.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class SummerTimeSprintBoatRecord(betterproto.Message):
    best_score: int = betterproto.uint32_field(3)
    start_time: int = betterproto.uint32_field(13)
    is_touched: bool = betterproto.bool_field(7)
    watcher_id_list: List[int] = betterproto.uint32_field(10)
    group_id: int = betterproto.uint32_field(2)
