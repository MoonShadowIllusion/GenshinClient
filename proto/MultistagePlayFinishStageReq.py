# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MultistagePlayFinishStageReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MultistagePlayFinishStageReq(betterproto.Message):
    """
    CmdId: 5398 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    group_id: int = betterproto.uint32_field(12)
    play_index: int = betterproto.uint32_field(15)