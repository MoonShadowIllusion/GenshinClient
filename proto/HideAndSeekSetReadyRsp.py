# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HideAndSeekSetReadyRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class HideAndSeekSetReadyRsp(betterproto.Message):
    """
    CmdId: 5370 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(11)
