# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_ICABIPHHPKE.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class Unk2700_ICABIPHHPKE(betterproto.Message):
    """
    CmdId: 8028 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__g_g_n_b_b_h_m_g_l_a_n: List[int] = betterproto.uint32_field(15)
    retcode: int = betterproto.int32_field(1)