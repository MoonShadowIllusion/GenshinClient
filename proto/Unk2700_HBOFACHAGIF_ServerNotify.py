# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_HBOFACHAGIF_ServerNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .Unk2700_EKDHFFHMNCD import *


@dataclass
class Unk2700_HBOFACHAGIF_ServerNotify(betterproto.Message):
    """
    CmdId: 9072 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__m_e_a_n_p_n_k_m_d_f_g: Dict[
        int, "Unk2700_EKDHFFHMNCD"
    ] = betterproto.map_field(2, betterproto.TYPE_UINT32, betterproto.TYPE_MESSAGE)
