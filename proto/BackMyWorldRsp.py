# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BackMyWorldRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class BackMyWorldRsp(betterproto.Message):
    """
    CmdId: 201 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(11)
