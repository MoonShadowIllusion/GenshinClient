# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_NMJIMIKKIME.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_HJLFNKLPFBH import *


@dataclass
class Unk2700_NMJIMIKKIME(betterproto.Message):
    """
    CmdId: 8943 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__o_k_g_k_h_p_c_m_n_m_n: List[int] = betterproto.uint32_field(9)
    unk2700__e_l_o_o_i_k_f_n_j_c_g: List[
        "Unk2700_HJLFNKLPFBH"
    ] = betterproto.message_field(11)
