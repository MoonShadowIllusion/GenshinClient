# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2800_IOBHBFFAONO.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_MOFABPNGIKP import *


@dataclass
class Unk2800_IOBHBFFAONO(betterproto.Message):
    param1: int = betterproto.uint32_field(7)
    param2: int = betterproto.uint32_field(2)
    reason: "Unk2700_MOFABPNGIKP" = betterproto.enum_field(3)
    param3: int = betterproto.uint32_field(6)
    unk2800__n_g_g_p_i_e_c_n_h_j_a: int = betterproto.uint32_field(12)
    gallery_id: int = betterproto.uint32_field(1)
