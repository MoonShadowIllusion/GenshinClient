# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChannelerSlabBuffSchemeInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class ChannelerSlabBuffSchemeInfo(betterproto.Message):
    slot_map: Dict[int, int] = betterproto.map_field(
        9, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    total_energy: int = betterproto.uint32_field(13)
    self_energy: int = betterproto.uint32_field(15)
