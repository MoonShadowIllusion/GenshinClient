# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_EJHALNBHHHD_ServerRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Unk2700_OPEBMJPOOBL import *


@dataclass
class Unk2700_EJHALNBHHHD_ServerRsp(betterproto.Message):
    """
    CmdId: 6322 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(15)
    unk2700__c_e_p_g_m_k_a_h_h_c_d: int = betterproto.uint64_field(8)
    unk2700__k_h_b_d_a_p_g_d_o_j_a: "Unk2700_OPEBMJPOOBL" = betterproto.enum_field(1)
