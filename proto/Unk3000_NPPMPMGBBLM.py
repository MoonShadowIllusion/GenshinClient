# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_NPPMPMGBBLM.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk3000_AHNHHIOAHBC import *


@dataclass
class Unk3000_NPPMPMGBBLM(betterproto.Message):
    """
    CmdId: 6368 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk3000__j_p_o_n_g_j_j_l_g_k_f: int = betterproto.uint32_field(7)
    unk3000__h_p_k_d_i_o_b_g_g_h_n: "Unk3000_AHNHHIOAHBC" = betterproto.enum_field(12)
    unk3000__o_a_f_a_k_p_m_j_c_e_n: "Unk3000_AHNHHIOAHBC" = betterproto.enum_field(15)
    unk3000__b_i_a_c_m_o_k_g_h_k_f: int = betterproto.uint32_field(8)
