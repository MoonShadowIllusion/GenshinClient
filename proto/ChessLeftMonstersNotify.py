# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChessLeftMonstersNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ChessLeftMonstersNotify(betterproto.Message):
    """
    CmdId: 5360 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    left_monsters: int = betterproto.uint32_field(6)
