# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FleurFairChapterInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class FleurFairChapterInfo(betterproto.Message):
    open_time: int = betterproto.uint32_field(15)
    chapter_id: int = betterproto.uint32_field(11)
