# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HideAndSeekPlayerReadyNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class HideAndSeekPlayerReadyNotify(betterproto.Message):
    """
    CmdId: 5302 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    uid_list: List[int] = betterproto.uint32_field(5)