# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: LunaRiteDetailInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .LunaRiteAreaInfo import *
from .LunaRiteHintPoint import *


@dataclass
class LunaRiteDetailInfo(betterproto.Message):
    hint_point: List["LunaRiteHintPoint"] = betterproto.message_field(3)
    area_info_list: List["LunaRiteAreaInfo"] = betterproto.message_field(13)
