# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BlitzRushParkourRestartRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class BlitzRushParkourRestartRsp(betterproto.Message):
    """
    CmdId: 8944 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(14)
    group_id: int = betterproto.uint32_field(15)
    schedule_id: int = betterproto.uint32_field(1)