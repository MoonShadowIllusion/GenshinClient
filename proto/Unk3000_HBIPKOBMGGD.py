# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_HBIPKOBMGGD.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk3000_HKHFFDEMNKN import *


@dataclass
class Unk3000_HBIPKOBMGGD(betterproto.Message):
    """
    CmdId: 5995 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk3000__g_c_j_l_j_c_j_a_a_d_g: List[
        "Unk3000_HKHFFDEMNKN"
    ] = betterproto.message_field(3)
