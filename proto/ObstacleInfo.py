# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ObstacleInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .MathQuaternion import *
from .Vector import *
from .Vector3Int import *


class ObstacleInfoShapeType(betterproto.Enum):
    SHAPE_TYPE_OBSTACLE_SHAPE_CAPSULE = 0
    SHAPE_TYPE_OBSTACLE_SHAPE_BOX = 1


@dataclass
class ObstacleInfo(betterproto.Message):
    rotation: "MathQuaternion" = betterproto.message_field(4)
    obstacle_id: int = betterproto.int32_field(2)
    center: "Vector" = betterproto.message_field(14)
    shape: "ObstacleInfoShapeType" = betterproto.enum_field(6)
    extents: "Vector3Int" = betterproto.message_field(12)
