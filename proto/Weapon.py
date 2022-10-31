# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Weapon.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class Weapon(betterproto.Message):
    level: int = betterproto.uint32_field(1)
    exp: int = betterproto.uint32_field(2)
    promote_level: int = betterproto.uint32_field(3)
    affix_map: Dict[int, int] = betterproto.map_field(
        4, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
