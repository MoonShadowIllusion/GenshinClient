# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_IIBHKLNAHHC.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk3000_IIBHKLNAHHC(betterproto.Message):
    level_id: int = betterproto.uint32_field(15)
    max_score: int = betterproto.uint32_field(9)
    is_open: bool = betterproto.bool_field(10)
