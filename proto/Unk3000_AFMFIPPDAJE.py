# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_AFMFIPPDAJE.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class Unk3000_AFMFIPPDAJE(betterproto.Message):
    """
    CmdId: 4576 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk3000__o_b_l_c_k_e_l_h_b_g_h: Dict[int, int] = betterproto.map_field(
        3, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    unk3000__l_o_f_n_f_m_j_f_g_n_b: int = betterproto.uint32_field(12)
