# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlantFlowerGetCanGiveFriendFlowerRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict

import betterproto


@dataclass
class PlantFlowerGetCanGiveFriendFlowerRsp(betterproto.Message):
    """
    CmdId: 8766 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    flower_num_map: Dict[int, int] = betterproto.map_field(
        6, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    schedule_id: int = betterproto.uint32_field(4)
    retcode: int = betterproto.int32_field(3)
