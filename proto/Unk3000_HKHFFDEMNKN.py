# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_HKHFFDEMNKN.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .WidgetSlotData import *


@dataclass
class Unk3000_HKHFFDEMNKN(betterproto.Message):
    uid: int = betterproto.uint32_field(14)
    slot_list: List["WidgetSlotData"] = betterproto.message_field(13)
