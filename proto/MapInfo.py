# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MapInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .CellInfo import *


@dataclass
class MapInfo(betterproto.Message):
    minx: int = betterproto.int32_field(1)
    maxx: int = betterproto.int32_field(2)
    minz: int = betterproto.int32_field(3)
    maxz: int = betterproto.int32_field(4)
    cells: List["CellInfo"] = betterproto.message_field(5)