# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_PMKNJBJPLBH.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_HJLFNKLPFBH import *


@dataclass
class Unk2700_PMKNJBJPLBH(betterproto.Message):
    """
    CmdId: 8385 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(11)
    unk2700__b_b_g_h_i_c_e_d_l_b_b: List[
        "Unk2700_HJLFNKLPFBH"
    ] = betterproto.message_field(13)
    unk2700__g_g_n_b_b_h_m_g_l_a_n: List[int] = betterproto.uint32_field(12)
    avatar_list: List["Unk2700_HJLFNKLPFBH"] = betterproto.message_field(9)