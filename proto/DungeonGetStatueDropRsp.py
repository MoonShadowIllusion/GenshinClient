# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonGetStatueDropRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DungeonGetStatueDropRsp(betterproto.Message):
    """
    CmdId: 904 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(12)
