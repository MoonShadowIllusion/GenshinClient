# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_GBPNAHCAKJE.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_EDNGHJGKEKC import *
from .Unk2700_LBPFDCBHCBL import *


@dataclass
class Unk2700_GBPNAHCAKJE(betterproto.Message):
    unk2700__o_a_k_b_d_k_k_b_f_h_p: str = betterproto.string_field(1)
    entity_id: str = betterproto.string_field(2)
    lang: str = betterproto.string_field(3)
    unk2700__n_d_e_j_p_m_g_p_b_a_h: str = betterproto.string_field(4)
    region: str = betterproto.string_field(5)
    uid: int = betterproto.uint32_field(6)
    unk2700__l_h_p_e_c_o_e_i_i_k_l: List[
        "Unk2700_EDNGHJGKEKC"
    ] = betterproto.message_field(7)
    unk2700__l_a_b_l_g_m_e_o_e_f_m: List[
        "Unk2700_LBPFDCBHCBL"
    ] = betterproto.message_field(8)
