# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SaveMainCoopReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class SaveMainCoopReq(betterproto.Message):
    """
    CmdId: 1975 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    normal_var_map: Dict[int, int] = betterproto.map_field(
        15, betterproto.TYPE_UINT32, betterproto.TYPE_INT32
    )
    self_confidence: int = betterproto.uint32_field(2)
    save_point_id: int = betterproto.uint32_field(1)
    temp_var_map: Dict[int, int] = betterproto.map_field(
        8, betterproto.TYPE_UINT32, betterproto.TYPE_INT32
    )
    id: int = betterproto.uint32_field(3)
