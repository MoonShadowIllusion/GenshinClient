# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SelectEffigyChallengeConditionReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class SelectEffigyChallengeConditionReq(betterproto.Message):
    """
    CmdId: 2064 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    difficulty_id: int = betterproto.uint32_field(15)
    challenge_id: int = betterproto.uint32_field(7)
    condition_id_list: List[int] = betterproto.uint32_field(9)
