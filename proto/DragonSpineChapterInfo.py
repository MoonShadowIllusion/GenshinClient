# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DragonSpineChapterInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DragonSpineChapterInfo(betterproto.Message):
    progress: int = betterproto.uint32_field(14)
    open_time: int = betterproto.uint32_field(6)
    is_open: bool = betterproto.bool_field(11)
    chapter_id: int = betterproto.uint32_field(9)
    finished_mission_num: int = betterproto.uint32_field(10)