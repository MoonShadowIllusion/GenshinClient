# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChessPickCardNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ChessNormalCardInfo import *


@dataclass
class ChessPickCardNotify(betterproto.Message):
    """
    CmdId: 5380 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    curse_card_id: int = betterproto.uint32_field(13)
    normal_card_info: "ChessNormalCardInfo" = betterproto.message_field(1)
