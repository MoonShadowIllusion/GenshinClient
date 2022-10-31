# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CodexTypeData.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto

from .CodexType import *


@dataclass
class CodexTypeData(betterproto.Message):
    codex_id_list: List[int] = betterproto.uint32_field(14)
    weapon_max_promote_level_map: Dict[int, int] = betterproto.map_field(
        4, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    type: "CodexType" = betterproto.enum_field(13)
    have_viewed_list: List[bool] = betterproto.bool_field(5)
