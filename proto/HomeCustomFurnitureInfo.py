# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeCustomFurnitureInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .CustomCommonNodeInfo import *


@dataclass
class HomeCustomFurnitureInfo(betterproto.Message):
    sub_furniture_list: List["CustomCommonNodeInfo"] = betterproto.message_field(12)
    guid: int = betterproto.uint32_field(6)