# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_INOMEGGAGOP.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_AIMMLILLOKB import *


@dataclass
class Unk2700_INOMEGGAGOP(betterproto.Message):
    """
    CmdId: 8132 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__d_f_g_c_i_b_j_f_n_b_c: List[
        "Unk2700_AIMMLILLOKB"
    ] = betterproto.message_field(5)
    schedule_id: int = betterproto.uint32_field(10)
    retcode: int = betterproto.int32_field(9)
