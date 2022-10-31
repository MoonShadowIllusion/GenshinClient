# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WorldPlayerLocationNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .PlayerLocationInfo import *
from .PlayerWorldLocationInfo import *


@dataclass
class WorldPlayerLocationNotify(betterproto.Message):
    """
    CmdId: 258 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    player_world_loc_list: List["PlayerWorldLocationInfo"] = betterproto.message_field(
        8
    )
    player_loc_list: List["PlayerLocationInfo"] = betterproto.message_field(15)
