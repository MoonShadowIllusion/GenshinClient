# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ReceivedTrialAvatarActivityRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ReceivedTrialAvatarActivityRewardReq(betterproto.Message):
    """
    CmdId: 2130 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    trial_avatar_index_id: int = betterproto.uint32_field(4)
