# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WorktopInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class WorktopInfo(betterproto.Message):
    option_list: List[int] = betterproto.uint32_field(1)
    is_guest_can_operate: bool = betterproto.bool_field(2)