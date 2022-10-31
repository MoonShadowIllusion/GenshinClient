# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TowerLevelStarCondNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .TowerLevelStarCondData import *


@dataclass
class TowerLevelStarCondNotify(betterproto.Message):
    """
    CmdId: 2406 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    level_index: int = betterproto.uint32_field(14)
    floor_id: int = betterproto.uint32_field(11)
    cond_data_list: List["TowerLevelStarCondData"] = betterproto.message_field(9)