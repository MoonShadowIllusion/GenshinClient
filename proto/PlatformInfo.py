# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlatformInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .MathQuaternion import *
from .MovingPlatformType import *
from .Route import *
from .Vector import *


@dataclass
class PlatformInfo(betterproto.Message):
    route_id: int = betterproto.uint32_field(1)
    start_index: int = betterproto.int32_field(2)
    start_route_time: int = betterproto.uint32_field(3)
    start_scene_time: int = betterproto.uint32_field(4)
    start_pos: "Vector" = betterproto.message_field(7)
    is_started: bool = betterproto.bool_field(8)
    start_rot: "MathQuaternion" = betterproto.message_field(9)
    stop_scene_time: int = betterproto.uint32_field(10)
    pos_offset: "Vector" = betterproto.message_field(11)
    rot_offset: "MathQuaternion" = betterproto.message_field(12)
    moving_platform_type: "MovingPlatformType" = betterproto.enum_field(13)
    is_active: bool = betterproto.bool_field(14)
    route: "Route" = betterproto.message_field(15)
    point_id: int = betterproto.uint32_field(16)
