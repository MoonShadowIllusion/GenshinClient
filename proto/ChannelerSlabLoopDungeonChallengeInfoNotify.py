# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChannelerSlabLoopDungeonChallengeInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ChannelerSlabLoopDungeonChallengeInfoNotify(betterproto.Message):
    """
    CmdId: 8224 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    dungeon_index: int = betterproto.uint32_field(12)
    challenge_score: int = betterproto.uint32_field(4)
    difficulty_id: int = betterproto.uint32_field(2)
    condition_id_list: List[int] = betterproto.uint32_field(3)
    scheme_buff_id_list: List[int] = betterproto.uint32_field(6)
