# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HitCollision.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .HitColliderType import *
from .Vector import *


@dataclass
class HitCollision(betterproto.Message):
    hit_collider_type: "HitColliderType" = betterproto.enum_field(8)
    hit_point: "Vector" = betterproto.message_field(7)
    attackee_hit_force_angle: float = betterproto.float_field(2)
    hit_dir: "Vector" = betterproto.message_field(13)
    attackee_hit_entity_angle: float = betterproto.float_field(15)
    hit_box_index: int = betterproto.int32_field(4)