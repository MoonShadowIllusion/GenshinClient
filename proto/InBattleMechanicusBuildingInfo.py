# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: InBattleMechanicusBuildingInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class InBattleMechanicusBuildingInfo(betterproto.Message):
    building_id: int = betterproto.uint32_field(8)
    level: int = betterproto.uint32_field(7)
    cost_points: int = betterproto.uint32_field(2)
    refund_points: int = betterproto.uint32_field(11)
