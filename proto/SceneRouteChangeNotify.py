# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneRouteChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .SceneRouteChangeInfo import *


@dataclass
class SceneRouteChangeNotify(betterproto.Message):
    """
    CmdId: 240 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    scene_id: int = betterproto.uint32_field(12)
    scene_time: int = betterproto.uint32_field(11)
    route_list: List["SceneRouteChangeInfo"] = betterproto.message_field(2)