# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ShapeBox.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class ShapeBox(betterproto.Message):
    center: "Vector" = betterproto.message_field(1)
    axis0: "Vector" = betterproto.message_field(2)
    axis1: "Vector" = betterproto.message_field(3)
    axis2: "Vector" = betterproto.message_field(4)
    extents: "Vector" = betterproto.message_field(5)
