# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ActivityUpdateWatcherNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .ActivityWatcherInfo import *


@dataclass
class ActivityUpdateWatcherNotify(betterproto.Message):
    """
    CmdId: 2156 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    watcher_info: "ActivityWatcherInfo" = betterproto.message_field(2)
    activity_id: int = betterproto.uint32_field(1)
