# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CellInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .SceneSurfaceMaterial import *


@dataclass
class CellInfo(betterproto.Message):
    type: "SceneSurfaceMaterial" = betterproto.enum_field(1)
    y: int = betterproto.int32_field(2)