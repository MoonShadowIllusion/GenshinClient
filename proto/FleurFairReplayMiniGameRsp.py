# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FleurFairReplayMiniGameRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class FleurFairReplayMiniGameRsp(betterproto.Message):
    """
    CmdId: 2052 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(14)
    minigame_id: int = betterproto.uint32_field(8)
