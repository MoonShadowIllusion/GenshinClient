# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WidgetCreatorInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .WidgetCreateLocationInfo import *
from .WidgetCreatorOpType import *


@dataclass
class WidgetCreatorInfo(betterproto.Message):
    op_type: "WidgetCreatorOpType" = betterproto.enum_field(10)
    entity_id: int = betterproto.uint32_field(1)
    location_info: "WidgetCreateLocationInfo" = betterproto.message_field(12)
