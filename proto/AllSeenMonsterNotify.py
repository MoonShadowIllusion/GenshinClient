# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AllSeenMonsterNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class AllSeenMonsterNotify(betterproto.Message):
    """
    CmdId: 271 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    monster_id_list: List[int] = betterproto.uint32_field(4)