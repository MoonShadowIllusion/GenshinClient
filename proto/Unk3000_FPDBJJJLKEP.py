# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_FPDBJJJLKEP.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk3000_BGPMEPKCLPA import *


@dataclass
class Unk3000_FPDBJJJLKEP(betterproto.Message):
    """
    CmdId: 6103 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk3000__a_d_j_j_o_g_d_k_i_k_l: "Unk3000_BGPMEPKCLPA" = betterproto.message_field(2)
    query_id: int = betterproto.int32_field(13)
    retcode: int = betterproto.int32_field(11)