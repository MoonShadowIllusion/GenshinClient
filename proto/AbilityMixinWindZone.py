# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AbilityMixinWindZone.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class AbilityMixinWindZone(betterproto.Message):
    entity_ids: List[int] = betterproto.uint32_field(13)
    zone_id_list: List[int] = betterproto.uint32_field(10)
