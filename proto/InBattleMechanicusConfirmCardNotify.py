# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: InBattleMechanicusConfirmCardNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class InBattleMechanicusConfirmCardNotify(betterproto.Message):
    """
    CmdId: 5348 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    play_index: int = betterproto.uint32_field(11)
    card_id: int = betterproto.uint32_field(13)
    group_id: int = betterproto.uint32_field(10)
    player_uid: int = betterproto.uint32_field(2)