# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MainCoop.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto


class MainCoopStatus(betterproto.Enum):
    STATUS_INVALID = 0
    STATUS_RUNNING = 1
    STATUS_FINISHED = 2


@dataclass
class MainCoop(betterproto.Message):
    seen_ending_map: Dict[int, int] = betterproto.map_field(
        13, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    normal_var_map: Dict[int, int] = betterproto.map_field(
        4, betterproto.TYPE_UINT32, betterproto.TYPE_INT32
    )
    self_confidence: int = betterproto.uint32_field(5)
    save_point_id_list: List[int] = betterproto.uint32_field(1)
    status: "MainCoopStatus" = betterproto.enum_field(6)
    temp_var_map: Dict[int, int] = betterproto.map_field(
        11, betterproto.TYPE_UINT32, betterproto.TYPE_INT32
    )
    id: int = betterproto.uint32_field(9)
