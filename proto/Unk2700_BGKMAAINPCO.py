# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_BGKMAAINPCO.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_JPGAAHJBLKB import *
from .Unk2700_PKAPCOBGIJL import *


@dataclass
class Unk2700_BGKMAAINPCO(betterproto.Message):
    unk2700__i_n_i_b_k_f_p_m_c_f_o: List[
        "Unk2700_PKAPCOBGIJL"
    ] = betterproto.message_field(2)
    avatar_info_list: List["Unk2700_JPGAAHJBLKB"] = betterproto.message_field(11)
