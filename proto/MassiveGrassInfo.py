# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MassiveGrassInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class MassiveGrassInfo(betterproto.Message):
    id: int = betterproto.uint32_field(1)
    center: "Vector" = betterproto.message_field(2)
    size: "Vector" = betterproto.message_field(3)
