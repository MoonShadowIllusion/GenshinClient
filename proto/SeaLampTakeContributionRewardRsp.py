# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SeaLampTakeContributionRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SeaLampTakeContributionRewardRsp(betterproto.Message):
    """
    CmdId: 2177 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    config_id: int = betterproto.uint32_field(9)
    retcode: int = betterproto.int32_field(7)
