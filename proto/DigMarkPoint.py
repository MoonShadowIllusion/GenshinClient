# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DigMarkPoint.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class DigMarkPoint(betterproto.Message):
    pos: "Vector" = betterproto.message_field(1)
    bundle_id: int = betterproto.uint32_field(13)
    rot: "Vector" = betterproto.message_field(3)
