# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChessPlayerInfoNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ChessPlayerInfo import *


@dataclass
class ChessPlayerInfoNotify(betterproto.Message):
    """
    CmdId: 5332 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    player_info: "ChessPlayerInfo" = betterproto.message_field(10)
