# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Vector.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Vector(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)
    z: float = betterproto.float_field(3)