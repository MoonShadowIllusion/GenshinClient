# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WidgetSlotData.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .WidgetSlotTag import *


@dataclass
class WidgetSlotData(betterproto.Message):
    cd_over_time: int = betterproto.uint32_field(9)
    tag: "WidgetSlotTag" = betterproto.enum_field(14)
    material_id: int = betterproto.uint32_field(11)
    is_active: bool = betterproto.bool_field(12)
