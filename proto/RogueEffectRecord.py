# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RogueEffectRecord.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class RogueEffectRecord(betterproto.Message):
    source_id: int = betterproto.uint32_field(6)
    extra_param_list: List[int] = betterproto.uint32_field(9)
    count: int = betterproto.uint32_field(10)
    is_new: bool = betterproto.bool_field(5)
