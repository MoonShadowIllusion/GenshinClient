# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PolygonRegionSize.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .VectorPlane import *


@dataclass
class PolygonRegionSize(betterproto.Message):
    point_list: List["VectorPlane"] = betterproto.message_field(5)
    height: float = betterproto.float_field(9)