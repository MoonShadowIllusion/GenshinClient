# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_HPFGNOIGNAG.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk3000_HPFGNOIGNAG(betterproto.Message):
    """
    CmdId: 21961 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk3000__p_h_i_i_b_c_m_n_p_e_k: bool = betterproto.bool_field(11)
    unk3000__n_f_l_e_i_n_a_b_p_p_c: bool = betterproto.bool_field(7)
    round: int = betterproto.uint32_field(15)
    stage_id: int = betterproto.uint32_field(8)
    level_id: int = betterproto.uint32_field(10)
