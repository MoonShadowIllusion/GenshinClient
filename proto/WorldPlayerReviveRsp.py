# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: WorldPlayerReviveRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class WorldPlayerReviveRsp(betterproto.Message):
    """
    CmdId: 278 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(3)