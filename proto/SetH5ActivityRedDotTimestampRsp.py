# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SetH5ActivityRedDotTimestampRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SetH5ActivityRedDotTimestampRsp(betterproto.Message):
    """
    CmdId: 5652 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(4)
