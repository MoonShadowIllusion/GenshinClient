# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MapAreaInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MapAreaInfo(betterproto.Message):
    map_area_id: int = betterproto.uint32_field(1)
    is_open: bool = betterproto.bool_field(2)
