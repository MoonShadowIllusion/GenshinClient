# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MistTrialGetChallengeMissionReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MistTrialGetChallengeMissionReq(betterproto.Message):
    """
    CmdId: 8893 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    trial_id: int = betterproto.uint32_field(9)
