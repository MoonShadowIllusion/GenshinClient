# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MiracleRingTakeRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MiracleRingTakeRewardRsp(betterproto.Message):
    """
    CmdId: 5202 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(14)
