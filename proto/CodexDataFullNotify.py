# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CodexDataFullNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .CodexTypeData import *


@dataclass
class CodexDataFullNotify(betterproto.Message):
    """
    CmdId: 4205 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__b_p_k_o_l_h_o_o_g_f_o: int = betterproto.uint32_field(4)
    unk2700__d_f_j_j_h_f_h_h_i_h_f: List[int] = betterproto.uint32_field(2)
    unk2700__h_j_d_n_b_b_p_m_o_a_p: int = betterproto.uint32_field(3)
    type_data_list: List["CodexTypeData"] = betterproto.message_field(6)
