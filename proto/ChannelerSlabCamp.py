# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChannelerSlabCamp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class ChannelerSlabCamp(betterproto.Message):
    reward_id: int = betterproto.uint32_field(11)
    pos: "Vector" = betterproto.message_field(8)
    buff_num: int = betterproto.uint32_field(7)
    group_id: int = betterproto.uint32_field(3)