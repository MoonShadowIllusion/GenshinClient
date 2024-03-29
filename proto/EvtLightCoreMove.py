# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtLightCoreMove.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class EvtLightCoreMove(betterproto.Message):
    target_pos: "Vector" = betterproto.message_field(15)
    acelerate: float = betterproto.float_field(11)
    entity_id: int = betterproto.uint32_field(5)
    max_absorb_time: float = betterproto.float_field(10)
    speed: float = betterproto.float_field(14)
