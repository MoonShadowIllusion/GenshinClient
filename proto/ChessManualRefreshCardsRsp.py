# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChessManualRefreshCardsRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ChessManualRefreshCardsRsp(betterproto.Message):
    """
    CmdId: 5359 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(12)
