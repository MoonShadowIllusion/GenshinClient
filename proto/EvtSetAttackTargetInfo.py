# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtSetAttackTargetInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class EvtSetAttackTargetInfo(betterproto.Message):
    entity_id: int = betterproto.uint32_field(11)
    unk2700__m_p_o_n_b_c_m_p_c_i_h: int = betterproto.uint32_field(6)
    attack_target_id: int = betterproto.uint32_field(7)
