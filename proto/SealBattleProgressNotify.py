# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SealBattleProgressNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SealBattleProgressNotify(betterproto.Message):
    """
    CmdId: 232 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    seal_entity_id: int = betterproto.uint32_field(9)
    max_progress: int = betterproto.uint32_field(10)
    seal_radius: int = betterproto.uint32_field(4)
    progress: int = betterproto.uint32_field(5)
    end_time: int = betterproto.uint32_field(2)
