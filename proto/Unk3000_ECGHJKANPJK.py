# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_ECGHJKANPJK.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk3000_ECGHJKANPJK(betterproto.Message):
    stage_id: int = betterproto.uint32_field(9)
    is_open: bool = betterproto.bool_field(1)
