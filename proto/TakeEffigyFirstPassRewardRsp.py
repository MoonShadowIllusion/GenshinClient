# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TakeEffigyFirstPassRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TakeEffigyFirstPassRewardRsp(betterproto.Message):
    """
    CmdId: 2061 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    challenge_id: int = betterproto.uint32_field(2)
    retcode: int = betterproto.int32_field(7)
