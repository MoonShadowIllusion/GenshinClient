# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_PKCLMDHHPFI.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_KIGGOKAEFHM import *


@dataclass
class Unk2700_PKCLMDHHPFI(betterproto.Message):
    """
    CmdId: 8423 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__h_h_o_d_m_c_c_n_g_k_e: List[
        "Unk2700_KIGGOKAEFHM"
    ] = betterproto.message_field(8)
    retcode: int = betterproto.int32_field(6)
