# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AiSkillCdInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class AiSkillCdInfo(betterproto.Message):
    skill_cd_map: Dict[int, int] = betterproto.map_field(
        11, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    skill_group_cd_map: Dict[int, int] = betterproto.map_field(
        6, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
