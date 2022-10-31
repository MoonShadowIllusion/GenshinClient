# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FoundationInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .FoundationStatus import *


@dataclass
class FoundationInfo(betterproto.Message):
    status: "FoundationStatus" = betterproto.enum_field(1)
    uid_list: List[int] = betterproto.uint32_field(2)
    current_building_id: int = betterproto.uint32_field(3)
    begin_build_time_ms: int = betterproto.uint32_field(4)