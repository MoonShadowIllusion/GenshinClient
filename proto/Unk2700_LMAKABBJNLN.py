# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_LMAKABBJNLN.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .Unk2700_FGJFFMPOJON import *


@dataclass
class Unk2700_LMAKABBJNLN(betterproto.Message):
    """
    CmdId: 8253 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(6)
    unk2700__c_o_o_f_m_k_l_n_b_n_d: List[
        "Unk2700_FGJFFMPOJON"
    ] = betterproto.message_field(11)
    schedule_id: int = betterproto.uint32_field(10)
