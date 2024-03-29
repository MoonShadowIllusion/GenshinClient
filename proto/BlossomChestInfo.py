# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BlossomChestInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class BlossomChestInfo(betterproto.Message):
    resin: int = betterproto.uint32_field(1)
    qualify_uid_list: List[int] = betterproto.uint32_field(2)
    remain_uid_list: List[int] = betterproto.uint32_field(3)
    dead_time: int = betterproto.uint32_field(4)
    blossom_refresh_type: int = betterproto.uint32_field(5)
    refresh_id: int = betterproto.uint32_field(6)
