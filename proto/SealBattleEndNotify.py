# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SealBattleEndNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SealBattleEndNotify(betterproto.Message):
    """
    CmdId: 259 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_win: bool = betterproto.bool_field(4)
    seal_entity_id: int = betterproto.uint32_field(15)