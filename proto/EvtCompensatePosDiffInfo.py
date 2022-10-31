# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtCompensatePosDiffInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class EvtCompensatePosDiffInfo(betterproto.Message):
    cur_pos: "Vector" = betterproto.message_field(14)
    entity_id: int = betterproto.uint32_field(11)
    face_angle_compact: int = betterproto.int32_field(10)
    cur_hash: int = betterproto.uint32_field(4)
    normalized_time_compact: int = betterproto.uint32_field(3)
