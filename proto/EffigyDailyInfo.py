# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EffigyDailyInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class EffigyDailyInfo(betterproto.Message):
    challenge_max_score: int = betterproto.uint32_field(6)
    is_first_pass_reward_taken: bool = betterproto.bool_field(12)
    challenge_total_score: int = betterproto.uint32_field(15)
    challenge_id: int = betterproto.uint32_field(1)
    challenge_count: int = betterproto.uint32_field(3)
    day_index: int = betterproto.uint32_field(14)
    begin_time: int = betterproto.uint32_field(2)