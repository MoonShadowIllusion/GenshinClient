# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChatChannelDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ChatChannelDataNotify(betterproto.Message):
    """
    CmdId: 4998 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    channel_list: List[int] = betterproto.uint32_field(3)