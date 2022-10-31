# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WatcherChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class WatcherChangeNotify(betterproto.Message):
    """
    CmdId: 2298 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    removed_watcher_list: List[int] = betterproto.uint32_field(2)
    new_watcher_list: List[int] = betterproto.uint32_field(15)