# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_MKMDOIKBBEP.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_HIHKGMLLOGD import *


@dataclass
class Unk2700_MKMDOIKBBEP(betterproto.Message):
    """
    CmdId: 8026 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__b_a_b_e_g_i_g_e_e_i_b: "Unk2700_HIHKGMLLOGD" = betterproto.message_field(
        10
    )
    retcode: int = betterproto.int32_field(5)
    unk2700__d_j_a_p_h_k_a_l_a_h_a: bool = betterproto.bool_field(1)
