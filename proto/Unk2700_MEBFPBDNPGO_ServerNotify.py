# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_MEBFPBDNPGO_ServerNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class Unk2700_MEBFPBDNPGO_ServerNotify(betterproto.Message):
    """
    CmdId: 4847 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__e_l_j_p_l_m_i_h_n_i_p: List[int] = betterproto.uint32_field(11)
