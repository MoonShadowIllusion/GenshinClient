# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RoguelikeTakeStageFirstPassRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RoguelikeTakeStageFirstPassRewardReq(betterproto.Message):
    """
    CmdId: 8421 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    stage_id: int = betterproto.uint32_field(1)
