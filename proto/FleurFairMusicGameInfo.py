# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FleurFairMusicGameInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .FleurFairMusicRecord import *


@dataclass
class FleurFairMusicGameInfo(betterproto.Message):
    music_record_map: Dict[int, "FleurFairMusicRecord"] = betterproto.map_field(
        10, betterproto.TYPE_UINT32, betterproto.TYPE_MESSAGE
    )