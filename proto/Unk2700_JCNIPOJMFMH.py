# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_JCNIPOJMFMH.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_EEPNCOAEKBM import *
from .Unk2700_LELADCCDNJH import *


@dataclass
class Unk2700_JCNIPOJMFMH(betterproto.Message):
    unk2700__o_c_b_d_o_d_a_g_p_n_f: List[
        "Unk2700_EEPNCOAEKBM"
    ] = betterproto.enum_field(12)
    level_list: List["Unk2700_LELADCCDNJH"] = betterproto.message_field(6)
    unk2700__e_g_p_c_j_l_g_g_g_l_k: List[int] = betterproto.uint32_field(10)
    unk2700__c_p_j_m_l_m_c_o_c_l_a: List[
        "Unk2700_EEPNCOAEKBM"
    ] = betterproto.enum_field(13)
