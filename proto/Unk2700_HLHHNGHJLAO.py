# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_HLHHNGHJLAO.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_MOFABPNGIKP import *


@dataclass
class Unk2700_HLHHNGHJLAO(betterproto.Message):
    kill_monster_count: int = betterproto.uint32_field(12)
    kill_special_monster_count: int = betterproto.uint32_field(8)
    unk2700__o_f_k_h_l_g_l_o_p_c_m: int = betterproto.uint32_field(10)
    gallery_id: int = betterproto.uint32_field(2)
    reason: "Unk2700_MOFABPNGIKP" = betterproto.enum_field(11)
    final_score: int = betterproto.uint32_field(13)
