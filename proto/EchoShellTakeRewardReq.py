# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EchoShellTakeRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class EchoShellTakeRewardReq(betterproto.Message):
    """
    CmdId: 8114 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    reward_id: int = betterproto.uint32_field(10)