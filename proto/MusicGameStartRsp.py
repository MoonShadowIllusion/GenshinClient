# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MusicGameStartRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MusicGameStartRsp(betterproto.Message):
    """
    CmdId: 8326 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    music_basic_id: int = betterproto.uint32_field(4)
    retcode: int = betterproto.int32_field(1)
    unk2700__c_e_p_g_m_k_a_h_h_c_d: int = betterproto.uint64_field(15)
