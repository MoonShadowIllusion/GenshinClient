# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SetPlayerBornDataRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SetPlayerBornDataRsp(betterproto.Message):
    """
    CmdId: 182 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(10)
