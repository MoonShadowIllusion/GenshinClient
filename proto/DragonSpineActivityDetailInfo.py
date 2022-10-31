# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DragonSpineActivityDetailInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .DragonSpineChapterInfo import *


@dataclass
class DragonSpineActivityDetailInfo(betterproto.Message):
    is_content_closed: bool = betterproto.bool_field(10)
    chapter_info_list: List["DragonSpineChapterInfo"] = betterproto.message_field(4)
    weapon_enhance_level: int = betterproto.uint32_field(2)
    content_finish_time: int = betterproto.uint32_field(15)
    shimmering_essence: int = betterproto.uint32_field(13)
    warm_essence: int = betterproto.uint32_field(11)
    wondrous_essence: int = betterproto.uint32_field(7)
