# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_GLAPMLGHDDC_ClientReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_NOCLNCCJEGK import *


@dataclass
class Unk2700_GLAPMLGHDDC_ClientReq(betterproto.Message):
    """
    CmdId: 5960 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    material_id: int = betterproto.uint32_field(14)
    unk2700__m_h_e_k_j_g_a_i_f_b_o: "Unk2700_NOCLNCCJEGK" = betterproto.enum_field(10)
    unk2700__g_m_h_l_h_k_i_i_g_i_c: int = betterproto.uint32_field(7)