# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_JMPCGMBHJLG.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_MLMEFKLMOEF import *


@dataclass
class Unk2700_JMPCGMBHJLG(betterproto.Message):
    unk2700__m_b_e_m_k_c_g_a_b_i_b: int = betterproto.uint32_field(3)
    unk2700__f_j_j_d_h_b_f_l_c_c_h: List[int] = betterproto.uint32_field(2)
    unk2700__j_d_b_f_o_i_l_o_o_i_f: List[
        "Unk2700_MLMEFKLMOEF"
    ] = betterproto.message_field(7)
