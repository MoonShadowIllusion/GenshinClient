# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_AIBHKIENDPF.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_BGKMAAINPCO import *


@dataclass
class Unk2700_AIBHKIENDPF(betterproto.Message):
    """
    CmdId: 8147 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    level_id: int = betterproto.uint32_field(1)
    difficulty_id: int = betterproto.uint32_field(14)
    retcode: int = betterproto.int32_field(6)
    unk2700__g_m_a_e_h_k_m_d_i_g_g: List[
        "Unk2700_BGKMAAINPCO"
    ] = betterproto.message_field(8)
