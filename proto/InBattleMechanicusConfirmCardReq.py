# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: InBattleMechanicusConfirmCardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class InBattleMechanicusConfirmCardReq(betterproto.Message):
    """
    CmdId: 5331 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    play_index: int = betterproto.uint32_field(6)
    card_id: int = betterproto.uint32_field(1)
    group_id: int = betterproto.uint32_field(3)
