# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HachiActivityDetailInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .HachiStageData import *


@dataclass
class HachiActivityDetailInfo(betterproto.Message):
    stage_map: Dict[int, "HachiStageData"] = betterproto.map_field(
        6, betterproto.TYPE_UINT32, betterproto.TYPE_MESSAGE
    )
