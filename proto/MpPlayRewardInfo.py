# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MpPlayRewardInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class MpPlayRewardInfo(betterproto.Message):
    resin: int = betterproto.uint32_field(1)
    remain_uid_list: List[int] = betterproto.uint32_field(2)
    qualify_uid_list: List[int] = betterproto.uint32_field(3)
