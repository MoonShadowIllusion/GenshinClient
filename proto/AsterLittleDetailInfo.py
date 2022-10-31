# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AsterLittleDetailInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .AsterLittleStageState import *


@dataclass
class AsterLittleDetailInfo(betterproto.Message):
    is_open: bool = betterproto.bool_field(4)
    stage_state: "AsterLittleStageState" = betterproto.enum_field(7)
    stage_id: int = betterproto.uint32_field(1)
    begin_time: int = betterproto.uint32_field(6)
    stage_begin_time: int = betterproto.uint32_field(5)
