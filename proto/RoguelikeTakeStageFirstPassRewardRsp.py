# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RoguelikeTakeStageFirstPassRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RoguelikeTakeStageFirstPassRewardRsp(betterproto.Message):
    """
    CmdId: 8552 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    stage_id: int = betterproto.uint32_field(14)
    retcode: int = betterproto.int32_field(5)