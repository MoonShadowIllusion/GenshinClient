# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SeeMonsterRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SeeMonsterRsp(betterproto.Message):
    """
    CmdId: 251 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(9)
