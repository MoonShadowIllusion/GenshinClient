# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_KEJGDDMMBLP.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk3000_PONJHEGKBBP import *


@dataclass
class Unk3000_KEJGDDMMBLP(betterproto.Message):
    """
    CmdId: 6376 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk3000__e_i_h_l_j_g_p_j_d_j_m: List[
        "Unk3000_PONJHEGKBBP"
    ] = betterproto.message_field(14)
