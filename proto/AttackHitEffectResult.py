# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AttackHitEffectResult.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AttackHitEffectResult(betterproto.Message):
    hit_halt_time_scale: float = betterproto.float_field(8)
    original_hit_eff_level: int = betterproto.uint32_field(12)
    air_strength: float = betterproto.float_field(15)
    hit_eff_level: int = betterproto.uint32_field(2)
    hit_halt_time: float = betterproto.float_field(13)
    retreat_strength: float = betterproto.float_field(7)
