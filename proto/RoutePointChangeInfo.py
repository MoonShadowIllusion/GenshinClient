# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RoutePointChangeInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RoutePointChangeInfo(betterproto.Message):
    wait_time: float = betterproto.float_field(6)
    target_velocity: float = betterproto.float_field(14)
    point_index: int = betterproto.uint32_field(11)
