# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WidgetCoolDownData.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class WidgetCoolDownData(betterproto.Message):
    is_success: bool = betterproto.bool_field(5)
    cool_down_time: int = betterproto.uint64_field(4)
    id: int = betterproto.uint32_field(15)