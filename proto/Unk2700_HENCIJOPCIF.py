# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_HENCIJOPCIF.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class Unk2700_HENCIJOPCIF(betterproto.Message):
    unk2700__e_m_i_e_l_b_m_c_c_p_f: int = betterproto.uint32_field(14)
    reward_item_list: List["ItemParam"] = betterproto.message_field(5)
