# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BlitzRushParkourRestartReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class BlitzRushParkourRestartReq(betterproto.Message):
    """
    CmdId: 8653 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    schedule_id: int = betterproto.uint32_field(13)
    group_id: int = betterproto.uint32_field(2)
