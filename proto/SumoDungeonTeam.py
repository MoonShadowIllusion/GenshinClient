# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SumoDungeonTeam.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .SumoDungeonAvatar import *


@dataclass
class SumoDungeonTeam(betterproto.Message):
    dungeon_avatar_list: List["SumoDungeonAvatar"] = betterproto.message_field(15)
