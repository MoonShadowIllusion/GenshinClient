# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayerInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ScenePlayerInfo import *


@dataclass
class ScenePlayerInfoNotify(betterproto.Message):
    """
    CmdId: 267 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    player_info_list: List["ScenePlayerInfo"] = betterproto.message_field(5)
