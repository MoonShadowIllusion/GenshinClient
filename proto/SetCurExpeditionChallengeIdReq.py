# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SetCurExpeditionChallengeIdReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SetCurExpeditionChallengeIdReq(betterproto.Message):
    """
    CmdId: 2021 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    id: int = betterproto.uint32_field(5)
