# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_AKIBKKOMBMC.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_IEPIBFMCJNJ import *


@dataclass
class Unk2700_AKIBKKOMBMC(betterproto.Message):
    """
    CmdId: 8120 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(15)
    unk2700__g_o_c_e_o_k_p_h_f_i_o: List[
        "Unk2700_IEPIBFMCJNJ"
    ] = betterproto.message_field(11)
    schedule_id: int = betterproto.uint32_field(6)
