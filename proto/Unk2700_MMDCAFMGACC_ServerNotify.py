# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_MMDCAFMGACC_ServerNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_ADGLMHECKKJ import *
from .Unk2700_KBBDJNLFAKD import *


@dataclass
class Unk2700_MMDCAFMGACC_ServerNotify(betterproto.Message):
    """
    CmdId: 6221 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__n_b_a_i_i_n_b_b_b_p_k: "Unk2700_ADGLMHECKKJ" = betterproto.enum_field(9)
    unk2700__e_i_o_p_o_p_a_b_b_n_c: List[int] = betterproto.uint32_field(14)
    unk2700__l_g_b_o_d_a_b_i_k_l_l: "Unk2700_KBBDJNLFAKD" = betterproto.enum_field(15)