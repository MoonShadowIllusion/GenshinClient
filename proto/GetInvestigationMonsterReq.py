# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetInvestigationMonsterReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class GetInvestigationMonsterReq(betterproto.Message):
    """
    CmdId: 1901 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    city_id_list: List[int] = betterproto.uint32_field(3)
    unk2700__d_e_m_f_d_h_n_f_b_b_j: bool = betterproto.bool_field(4)
