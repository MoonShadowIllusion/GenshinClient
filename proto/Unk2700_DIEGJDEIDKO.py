# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_DIEGJDEIDKO.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class Unk2700_DIEGJDEIDKO(betterproto.Message):
    cur_progress: int = betterproto.uint32_field(12)
    id: int = betterproto.uint32_field(6)
    open_time: int = betterproto.uint32_field(8)
    is_finished: bool = betterproto.bool_field(10)
    total_progress: int = betterproto.uint32_field(9)
    pos: "Vector" = betterproto.message_field(5)
