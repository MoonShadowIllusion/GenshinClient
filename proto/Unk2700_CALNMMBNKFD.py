# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_CALNMMBNKFD.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_AIMMLILLOKB import *


@dataclass
class Unk2700_CALNMMBNKFD(betterproto.Message):
    """
    CmdId: 8502 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__g_h_d_h_i_b_d_l_f_p_n: "Unk2700_AIMMLILLOKB" = betterproto.message_field(4)
    retcode: int = betterproto.int32_field(11)
    schedule_id: int = betterproto.uint32_field(10)
