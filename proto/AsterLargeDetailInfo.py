# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AsterLargeDetailInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AsterLargeDetailInfo(betterproto.Message):
    is_open: bool = betterproto.bool_field(3)
    begin_time: int = betterproto.uint32_field(13)
