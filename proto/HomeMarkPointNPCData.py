# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeMarkPointNPCData.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class HomeMarkPointNPCData(betterproto.Message):
    avatar_id: int = betterproto.uint32_field(1)
    costume_id: int = betterproto.uint32_field(2)