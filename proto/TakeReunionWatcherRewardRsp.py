# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TakeReunionWatcherRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TakeReunionWatcherRewardRsp(betterproto.Message):
    """
    CmdId: 5095 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    mission_id: int = betterproto.uint32_field(15)
    watcher_id: int = betterproto.uint32_field(9)
    retcode: int = betterproto.int32_field(10)
