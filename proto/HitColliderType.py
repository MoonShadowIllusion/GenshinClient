# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HitColliderType.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class HitColliderType(betterproto.Enum):
    HIT_COLLIDER_TYPE_INVALID = 0
    HIT_COLLIDER_TYPE_HIT_BOX = 1
    HIT_COLLIDER_TYPE_WET_HIT_BOX = 2
    HIT_COLLIDER_TYPE_HEAD_BOX = 3