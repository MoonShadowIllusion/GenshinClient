# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarSkillInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class AvatarSkillInfo(betterproto.Message):
    pass_cd_time: int = betterproto.uint32_field(1)
    full_cd_time_list: List[int] = betterproto.uint32_field(2)
    max_charge_count: int = betterproto.uint32_field(3)