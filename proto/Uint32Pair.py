# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Uint32Pair.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Uint32Pair(betterproto.Message):
    key: int = betterproto.uint32_field(1)
    value: int = betterproto.uint32_field(2)
