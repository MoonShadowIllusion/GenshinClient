# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeResource.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class HomeResource(betterproto.Message):
    next_refresh_time: float = betterproto.fixed32_field(15)
    store_limit: int = betterproto.uint32_field(3)
    store_value: int = betterproto.uint32_field(12)
