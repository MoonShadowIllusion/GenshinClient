# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: StopServerInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class StopServerInfo(betterproto.Message):
    stop_begin_time: int = betterproto.uint32_field(1)
    stop_end_time: int = betterproto.uint32_field(2)
    url: str = betterproto.string_field(3)
    content_msg: str = betterproto.string_field(4)
