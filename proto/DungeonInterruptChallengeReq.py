# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonInterruptChallengeReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DungeonInterruptChallengeReq(betterproto.Message):
    """
    CmdId: 917 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    challenge_index: int = betterproto.uint32_field(14)
    group_id: int = betterproto.uint32_field(13)
    challenge_id: int = betterproto.uint32_field(11)
