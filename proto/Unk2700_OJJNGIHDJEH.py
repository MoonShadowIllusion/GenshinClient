# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_OJJNGIHDJEH.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_OCDMIOKNHHH import *


@dataclass
class Unk2700_OJJNGIHDJEH(betterproto.Message):
    unk2700__o_m_c_c_f_b_b_d_j_m_i: int = betterproto.uint32_field(1)
    timestamp: int = betterproto.uint32_field(8)
    player_info: "Unk2700_OCDMIOKNHHH" = betterproto.message_field(12)
