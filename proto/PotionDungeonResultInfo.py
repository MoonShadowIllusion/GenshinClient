# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PotionDungeonResultInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PotionDungeonResultInfo(betterproto.Message):
    final_score: int = betterproto.uint32_field(8)
    left_time: int = betterproto.uint32_field(9)
    unk2700__f_h_e_h_g_d_a_b_a_l_e: int = betterproto.uint32_field(14)
    unk2700__h_k_f_e_b_b_c_m_b_h_l: int = betterproto.uint32_field(11)
    level_id: int = betterproto.uint32_field(4)
    stage_id: int = betterproto.uint32_field(2)