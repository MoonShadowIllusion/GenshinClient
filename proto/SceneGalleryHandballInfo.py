# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneGalleryHandballInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .PlaceInfo import *


@dataclass
class SceneGalleryHandballInfo(betterproto.Message):
    ball_place_info: "PlaceInfo" = betterproto.message_field(9)
    is_have_ball: bool = betterproto.bool_field(15)
