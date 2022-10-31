# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ReunionBriefInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ReunionBriefInfo(betterproto.Message):
    is_taken_first_gift: bool = betterproto.bool_field(8)
    mission_has_reward: bool = betterproto.bool_field(9)
    privilege_id: int = betterproto.uint32_field(5)
    start_time: int = betterproto.uint32_field(7)
    version: str = betterproto.string_field(13)
    sign_in_has_reward: bool = betterproto.bool_field(2)
    first_gift_reward_id: int = betterproto.uint32_field(15)
    mission_id: int = betterproto.uint32_field(10)
    first_day_start_time: int = betterproto.uint32_field(3)
    sign_in_config_id: int = betterproto.uint32_field(6)
    finish_time: int = betterproto.uint32_field(12)