# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ShapeSphere.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class ShapeSphere(betterproto.Message):
    center: "Vector" = betterproto.message_field(1)
    radius: float = betterproto.float_field(2)
