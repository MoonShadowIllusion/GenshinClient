# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class DungeonDataNotify(betterproto.Message):
    """
    CmdId: 982 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    dungeon_data_map: Dict[int, int] = betterproto.map_field(
        1, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
