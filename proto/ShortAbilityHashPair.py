# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ShortAbilityHashPair.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ShortAbilityHashPair(betterproto.Message):
    ability_config_hash: float = betterproto.sfixed32_field(15)
    ability_name_hash: float = betterproto.sfixed32_field(1)