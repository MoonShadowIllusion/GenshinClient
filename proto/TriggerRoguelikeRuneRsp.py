# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TriggerRoguelikeRuneRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TriggerRoguelikeRuneRsp(betterproto.Message):
    """
    CmdId: 8065 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    available_count: int = betterproto.uint32_field(4)
    rune_id: int = betterproto.uint32_field(14)
    retcode: int = betterproto.int32_field(8)
