# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerQuitDungeonRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PlayerQuitDungeonRsp(betterproto.Message):
    """
    CmdId: 921 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    point_id: int = betterproto.uint32_field(11)
    retcode: int = betterproto.int32_field(7)
