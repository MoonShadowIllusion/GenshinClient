# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChannelerSlabLoopDungeonSelectConditionRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ChannelerSlabLoopDungeonSelectConditionRsp(betterproto.Message):
    """
    CmdId: 8509 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(9)
    dungeon_index: int = betterproto.uint32_field(5)
    condition_id_list: List[int] = betterproto.uint32_field(13)
    difficulty_id: int = betterproto.uint32_field(14)