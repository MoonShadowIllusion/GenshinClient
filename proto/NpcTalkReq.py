# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: NpcTalkReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class NpcTalkReq(betterproto.Message):
    """
    CmdId: 572 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(8)
    npc_entity_id: int = betterproto.uint32_field(9)
    talk_id: int = betterproto.uint32_field(7)
