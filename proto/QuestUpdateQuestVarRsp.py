# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: QuestUpdateQuestVarRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class QuestUpdateQuestVarRsp(betterproto.Message):
    """
    CmdId: 439 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(10)
    parent_quest_var_seq: int = betterproto.uint32_field(2)
    parent_quest_id: int = betterproto.uint32_field(8)
    quest_id: int = betterproto.uint32_field(15)
