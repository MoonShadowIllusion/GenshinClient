# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FindHilichurlFinishSecondQuestNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class FindHilichurlFinishSecondQuestNotify(betterproto.Message):
    """
    CmdId: 8901 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    day_index: int = betterproto.uint32_field(11)
