# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_DCLAGIJJEHB.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk3000_ENLDIHLGNCK import *


@dataclass
class Unk3000_DCLAGIJJEHB(betterproto.Message):
    """
    CmdId: 402 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    parent_quest_id: int = betterproto.uint32_field(2)
    unk3000__h_l_p_g_i_l_i_g_g_c_b: List[
        "Unk3000_ENLDIHLGNCK"
    ] = betterproto.message_field(1)