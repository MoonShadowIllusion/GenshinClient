# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlantFlowerSetFlowerWishReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class PlantFlowerSetFlowerWishReq(betterproto.Message):
    """
    CmdId: 8547 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    flower_num_map: Dict[int, int] = betterproto.map_field(
        12, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    schedule_id: int = betterproto.uint32_field(5)
