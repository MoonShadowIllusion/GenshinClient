# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: StrengthenPointData.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class StrengthenPointData(betterproto.Message):
    base_point: int = betterproto.uint32_field(10)
    cur_point: int = betterproto.uint32_field(11)