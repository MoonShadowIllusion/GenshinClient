# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PullRecentChatReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PullRecentChatReq(betterproto.Message):
    """
    CmdId: 5040 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    pull_num: int = betterproto.uint32_field(6)
    begin_sequence: int = betterproto.uint32_field(15)
