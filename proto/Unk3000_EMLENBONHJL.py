# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_EMLENBONHJL.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk3000_HDJHHOCABBK import *


@dataclass
class Unk3000_EMLENBONHJL(betterproto.Message):
    treasure_close_time: int = betterproto.uint32_field(10)
    is_content_closed: bool = betterproto.bool_field(8)
    unk3000__n_m_e_p_j_a_n_n_l_l_e: List[
        "Unk3000_HDJHHOCABBK"
    ] = betterproto.message_field(14)
