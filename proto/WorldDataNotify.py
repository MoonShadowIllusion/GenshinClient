# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WorldDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto

from .PropValue import *


class WorldDataNotifyDataType(betterproto.Enum):
    DATA_TYPE_NONE = 0
    DATA_TYPE_WORLD_LEVEL = 1
    DATA_TYPE_IS_IN_MP_MODE = 2


@dataclass
class WorldDataNotify(betterproto.Message):
    """
    CmdId: 3308 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    world_prop_map: Dict[int, "PropValue"] = betterproto.map_field(
        9, betterproto.TYPE_UINT32, betterproto.TYPE_MESSAGE
    )
