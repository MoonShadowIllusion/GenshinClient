# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2800_MHCFAGCKGIB.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .DungeonEntryInfo import *


@dataclass
class Unk2800_MHCFAGCKGIB(betterproto.Message):
    scene_id: int = betterproto.uint32_field(12)
    point_id: int = betterproto.uint32_field(6)
    dungeon_entry_list: List["DungeonEntryInfo"] = betterproto.message_field(1)
    recommend_dungeon_id: int = betterproto.uint32_field(8)
