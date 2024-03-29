# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChessEntranceInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ChessMonsterInfo import *


@dataclass
class ChessEntranceInfo(betterproto.Message):
    monster_info_list: List["ChessMonsterInfo"] = betterproto.message_field(14)
    entrance_index: int = betterproto.uint32_field(15)
    entrance_point_id: int = betterproto.uint32_field(8)
