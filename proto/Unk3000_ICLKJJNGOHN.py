# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_ICLKJJNGOHN.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk3000_KEJLPBEOHNH import *


@dataclass
class Unk3000_ICLKJJNGOHN(betterproto.Message):
    is_finished: bool = betterproto.bool_field(10)
    max_score: int = betterproto.uint32_field(3)
    stage_id: int = betterproto.uint32_field(4)
    unk2700__g_m_a_e_h_k_m_d_i_g_g: List[
        "Unk3000_KEJLPBEOHNH"
    ] = betterproto.message_field(6)
