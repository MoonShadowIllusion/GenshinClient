# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MapAreaChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .MapAreaInfo import *


@dataclass
class MapAreaChangeNotify(betterproto.Message):
    """
    CmdId: 3378 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    map_area_info_list: List["MapAreaInfo"] = betterproto.message_field(3)
