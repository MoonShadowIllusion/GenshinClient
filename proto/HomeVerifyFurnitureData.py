# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeVerifyFurnitureData.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class HomeVerifyFurnitureData(betterproto.Message):
    type: List[int] = betterproto.uint32_field(7)
    id: int = betterproto.uint32_field(5)
    num: int = betterproto.uint32_field(9)
