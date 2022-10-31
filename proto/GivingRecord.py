# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GivingRecord.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class GivingRecord(betterproto.Message):
    is_finished: bool = betterproto.bool_field(9)
    group_id: int = betterproto.uint32_field(5)
    unk2800__j_b_p_p_n_e_h_p_a_c_c: bool = betterproto.bool_field(8)
    giving_id: int = betterproto.uint32_field(3)
    last_group_id: int = betterproto.uint32_field(6)
    config_id: int = betterproto.uint32_field(2)
    unk2800__b_d_k_k_e_n_p_e_e_g_d: Dict[int, int] = betterproto.map_field(
        15, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )