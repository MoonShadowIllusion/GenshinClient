# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_GEIGCHNDOAA.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_IMGLPJNBHCH import *


@dataclass
class Unk2700_GEIGCHNDOAA(betterproto.Message):
    """
    CmdId: 8657 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    stage_id: int = betterproto.uint32_field(7)
    unk2700__l_n_i_n_c_i_b_p_i_b_n: bool = betterproto.bool_field(13)
    challenge_id: int = betterproto.uint32_field(8)
    unk2700__d_m_j_o_j_p_g_l_f_h_e: List[
        "Unk2700_IMGLPJNBHCH"
    ] = betterproto.message_field(2)
    unk2700__h_m_i_b_i_i_p_h_b_a_n: int = betterproto.uint32_field(10)
    unk2700__l_o_i_m_a_g_f_k_m_o_j: int = betterproto.uint32_field(15)
    unk2700__f_g_i_i_b_j_a_d_e_c_i: int = betterproto.uint32_field(11)
    retcode: int = betterproto.int32_field(3)
    unk2700__a_e_h_o_p_m_m_m_h_a_p: int = betterproto.uint32_field(12)
