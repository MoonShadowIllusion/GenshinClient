# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ClientCollectorData.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ClientCollectorData(betterproto.Message):
    material_id: int = betterproto.uint32_field(10)
    max_points: int = betterproto.uint32_field(8)
    curr_points: int = betterproto.uint32_field(13)