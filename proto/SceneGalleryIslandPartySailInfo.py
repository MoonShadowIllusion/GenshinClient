# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneGalleryIslandPartySailInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2800_FMAOEPEBKHB import *
from .Unk2800_IMLDGLIMODE import *


@dataclass
class SceneGalleryIslandPartySailInfo(betterproto.Message):
    unk2800__h_k_h_e_n_l_c_i_f_n_n: int = betterproto.uint32_field(14)
    unk2800__n_g_p_l_g_l_l_f_g_o_g: int = betterproto.uint32_field(10)
    unk2800__e_n_j_g_e_f_b_c_l_o_l: "Unk2800_FMAOEPEBKHB" = betterproto.enum_field(1)
    unk2800__d_n_d_k_j_o_j_c_d_b_i: int = betterproto.uint32_field(11)
    coin: int = betterproto.uint32_field(15)
    stage: "Unk2800_IMLDGLIMODE" = betterproto.enum_field(12)
    unk2800__g_m_o_c_m_e_f_b_g_i_p: int = betterproto.uint32_field(8)
