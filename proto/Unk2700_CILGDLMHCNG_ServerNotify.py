# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_CILGDLMHCNG_ServerNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_CILGDLMHCNG_ServerNotify(betterproto.Message):
    """
    CmdId: 1951 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    unk2700__g_e_b_o_k_a_m_g_e_e_b: str = betterproto.string_field(7)
    chapter_id: int = betterproto.uint32_field(15)
