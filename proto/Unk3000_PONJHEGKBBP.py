# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_PONJHEGKBBP.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .Unk3000_AHNHHIOAHBC import *


@dataclass
class Unk3000_PONJHEGKBBP(betterproto.Message):
    unk3000__m_k_n_o_d_e_k_e_g_j_f: Dict[
        int, "Unk3000_AHNHHIOAHBC"
    ] = betterproto.map_field(6, betterproto.TYPE_UINT32, betterproto.TYPE_ENUM)
    unk3000__j_p_o_n_g_j_j_l_g_k_f: int = betterproto.uint32_field(12)
