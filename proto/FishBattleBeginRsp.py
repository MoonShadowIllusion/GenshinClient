# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FishBattleBeginRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class FishBattleBeginRsp(betterproto.Message):
    """
    CmdId: 5845 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(10)
