# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EntityEnvironmentInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class EntityEnvironmentInfo(betterproto.Message):
    json_climate_type: int = betterproto.uint32_field(1)
    climate_area_id: int = betterproto.uint32_field(2)
