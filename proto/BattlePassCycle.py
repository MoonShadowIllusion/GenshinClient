# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BattlePassCycle.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class BattlePassCycle(betterproto.Message):
    cycle_idx: int = betterproto.uint32_field(3)
    end_time: int = betterproto.uint32_field(10)
    begin_time: int = betterproto.uint32_field(13)