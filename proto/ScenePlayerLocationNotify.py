# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayerLocationNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .PlayerLocationInfo import *
from .VehicleLocationInfo import *


@dataclass
class ScenePlayerLocationNotify(betterproto.Message):
    """CmdId: 248 EnetChannelId: 0 EnetIsReliable: true IsAllowClient: true"""

    vehicle_loc_list: List["VehicleLocationInfo"] = betterproto.message_field(3)
    scene_id: int = betterproto.uint32_field(9)
    player_loc_list: List["PlayerLocationInfo"] = betterproto.message_field(14)
