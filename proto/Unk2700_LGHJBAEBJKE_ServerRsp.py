# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_LGHJBAEBJKE_ServerRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_MIBBHAEMAGI import *
from .Unk2700_OGKIDNPMMKG import *


@dataclass
class Unk2700_LGHJBAEBJKE_ServerRsp(betterproto.Message):
    """
    CmdId: 6227 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(10)
    unk2700__h_k_i_f_d_f_g_h_j_o_k: "Unk2700_OGKIDNPMMKG" = betterproto.message_field(
        14
    )
    unk2700__k_l_o_a_f_p_m_h_o_k_i: List[
        "Unk2700_MIBBHAEMAGI"
    ] = betterproto.message_field(5)
