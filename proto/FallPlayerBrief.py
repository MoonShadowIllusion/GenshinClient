# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FallPlayerBrief.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class FallPlayerBrief(betterproto.Message):
    uid: int = betterproto.uint32_field(13)
    is_ground: bool = betterproto.bool_field(5)
    score: int = betterproto.uint32_field(10)
