# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChannelerSlabLoopDungeonSelectConditionReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ChannelerSlabLoopDungeonSelectConditionReq(betterproto.Message):
    """
    CmdId: 8503 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    dungeon_index: int = betterproto.uint32_field(4)
    condition_id_list: List[int] = betterproto.uint32_field(3)
    difficulty_id: int = betterproto.uint32_field(8)