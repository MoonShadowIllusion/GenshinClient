# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityMixinShieldBar.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AbilityMixinShieldBar(betterproto.Message):
    unk2700__p_b_k_b_d_d_l_n_b_e_a: int = betterproto.uint32_field(14)
    max_shield: float = betterproto.float_field(15)
    shield: float = betterproto.float_field(12)
    element_type: int = betterproto.uint32_field(13)
