# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: LuminanceStoneChallengeActivityDetailInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class LuminanceStoneChallengeActivityDetailInfo(betterproto.Message):
    best_score: int = betterproto.uint32_field(11)
    is_content_closed: bool = betterproto.bool_field(6)
    unk2700__c_k_g_m_n_l_p_d_f_c_i: bool = betterproto.bool_field(12)
    unk2700__n_n_l_b_i_a_f_m_h_p_a: int = betterproto.uint32_field(15)