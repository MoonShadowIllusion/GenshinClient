# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_FLOEPMMABMH.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk3000_FLOEPMMABMH(betterproto.Message):
    level_id: int = betterproto.uint32_field(13)
    max_score: int = betterproto.uint32_field(14)
    is_open: bool = betterproto.bool_field(1)
