# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FleurFairMinigameInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .FleurFairBalloonInfo import *
from .FleurFairFallInfo import *
from .FleurFairMusicGameInfo import *


@dataclass
class FleurFairMinigameInfo(betterproto.Message):
    minigame_id: int = betterproto.uint32_field(13)
    is_open: bool = betterproto.bool_field(8)
    open_time: int = betterproto.uint32_field(15)
    balloon_info: "FleurFairBalloonInfo" = betterproto.message_field(12, group="detail")
    fall_info: "FleurFairFallInfo" = betterproto.message_field(11, group="detail")
    music_info: "FleurFairMusicGameInfo" = betterproto.message_field(9, group="detail")