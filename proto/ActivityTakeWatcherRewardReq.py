# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ActivityTakeWatcherRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ActivityTakeWatcherRewardReq(betterproto.Message):
    """
    CmdId: 2038 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    activity_id: int = betterproto.uint32_field(4)
    watcher_id: int = betterproto.uint32_field(14)
