# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PropValue.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PropValue(betterproto.Message):
    type: int = betterproto.uint32_field(1)
    val: int = betterproto.int64_field(4)
    ival: int = betterproto.int64_field(2, group="value")
    fval: float = betterproto.float_field(3, group="value")