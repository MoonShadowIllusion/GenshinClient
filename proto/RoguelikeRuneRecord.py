# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RoguelikeRuneRecord.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RoguelikeRuneRecord(betterproto.Message):
    left_count: int = betterproto.uint32_field(14)
    rune_id: int = betterproto.uint32_field(6)
    max_count: int = betterproto.uint32_field(4)