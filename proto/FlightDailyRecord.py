# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FlightDailyRecord.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class FlightDailyRecord(betterproto.Message):
    group_id: int = betterproto.uint32_field(4)
    is_touched: bool = betterproto.bool_field(1)
    watcher_id_list: List[int] = betterproto.uint32_field(11)
    best_score: int = betterproto.uint32_field(7)
    start_time: int = betterproto.uint32_field(3)
