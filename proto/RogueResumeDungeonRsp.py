# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RogueResumeDungeonRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RogueResumeDungeonRsp(betterproto.Message):
    """
    CmdId: 8647 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    stage_id: int = betterproto.uint32_field(12)
    retcode: int = betterproto.int32_field(15)