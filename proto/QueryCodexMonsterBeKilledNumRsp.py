# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: QueryCodexMonsterBeKilledNumRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class QueryCodexMonsterBeKilledNumRsp(betterproto.Message):
    """
    CmdId: 4209 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    codex_id_list: List[int] = betterproto.uint32_field(4)
    unk2700__m_k_o_b_m_g_g_p_n_m_i: List[int] = betterproto.uint32_field(6)
    be_killed_num_list: List[int] = betterproto.uint32_field(12)
    retcode: int = betterproto.int32_field(5)
