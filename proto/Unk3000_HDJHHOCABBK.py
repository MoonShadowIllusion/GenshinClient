# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_HDJHHOCABBK.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class Unk3000_HDJHHOCABBK(betterproto.Message):
    is_done: bool = betterproto.bool_field(12)
    unk3000__l_i_h_p_a_b_k_o_a_i_p: int = betterproto.uint32_field(6)
    unk3000__a_e_g_h_m_l_l_e_o_j_f: int = betterproto.uint32_field(10)
    region_radius: float = betterproto.float_field(7)
    is_open: bool = betterproto.bool_field(9)
    open_time: int = betterproto.uint32_field(8)
    region_center_pos: "Vector" = betterproto.message_field(11)
    scene_id: int = betterproto.uint32_field(13)
    unk3000__k_n_n_p_m_a_m_o_c_o_m: int = betterproto.uint32_field(15)
    region_id: int = betterproto.uint32_field(1)
