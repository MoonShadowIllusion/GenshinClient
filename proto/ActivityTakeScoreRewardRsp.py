# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ActivityTakeScoreRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ActivityTakeScoreRewardRsp(betterproto.Message):
    """
    CmdId: 8583 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    activity_id: int = betterproto.uint32_field(13)
    retcode: int = betterproto.int32_field(9)
    reward_config_id: int = betterproto.uint32_field(15)
