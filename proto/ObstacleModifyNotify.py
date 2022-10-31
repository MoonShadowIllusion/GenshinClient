# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ObstacleModifyNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ObstacleInfo import *


@dataclass
class ObstacleModifyNotify(betterproto.Message):
    """
    CmdId: 2312 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    remove_obstacle_ids: List[int] = betterproto.int32_field(9)
    add_obstacles: List["ObstacleInfo"] = betterproto.message_field(6)
    scene_id: int = betterproto.uint32_field(5)
