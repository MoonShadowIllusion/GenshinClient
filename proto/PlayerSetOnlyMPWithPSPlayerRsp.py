# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerSetOnlyMPWithPSPlayerRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PlayerSetOnlyMPWithPSPlayerRsp(betterproto.Message):
    """
    CmdId: 1845 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(5)
    is_only: bool = betterproto.bool_field(8)
