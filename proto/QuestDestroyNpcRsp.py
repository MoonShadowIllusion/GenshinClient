# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: QuestDestroyNpcRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class QuestDestroyNpcRsp(betterproto.Message):
    """
    CmdId: 465 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    npc_id: int = betterproto.uint32_field(12)
    parent_quest_id: int = betterproto.uint32_field(4)
    retcode: int = betterproto.int32_field(5)
