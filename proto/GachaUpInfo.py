# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GachaUpInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class GachaUpInfo(betterproto.Message):
    item_parent_type: int = betterproto.uint32_field(7)
    item_id_list: List[int] = betterproto.uint32_field(15)
