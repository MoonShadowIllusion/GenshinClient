# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: QuestUpdateQuestVarNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class QuestUpdateQuestVarNotify(betterproto.Message):
    """
    CmdId: 453 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    quest_var: List[int] = betterproto.int32_field(1)
    parent_quest_id: int = betterproto.uint32_field(12)
    parent_quest_var_seq: int = betterproto.uint32_field(8)
