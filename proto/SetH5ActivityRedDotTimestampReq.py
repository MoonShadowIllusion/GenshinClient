# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SetH5ActivityRedDotTimestampReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SetH5ActivityRedDotTimestampReq(betterproto.Message):
    """
    CmdId: 5657 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    client_red_dot_timestamp: int = betterproto.uint32_field(13)
