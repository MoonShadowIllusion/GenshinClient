# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerForceExitRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PlayerForceExitRsp(betterproto.Message):
    """
    CmdId: 159 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(15)
