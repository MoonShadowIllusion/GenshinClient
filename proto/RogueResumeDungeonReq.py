# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RogueResumeDungeonReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RogueResumeDungeonReq(betterproto.Message):
    """
    CmdId: 8795 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    stage_id: int = betterproto.uint32_field(12)
