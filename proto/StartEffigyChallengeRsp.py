# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: StartEffigyChallengeRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class StartEffigyChallengeRsp(betterproto.Message):
    """
    CmdId: 2173 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    condition_id_list: List[int] = betterproto.uint32_field(2)
    retcode: int = betterproto.int32_field(8)
    challenge_id: int = betterproto.uint32_field(15)
    difficulty_id: int = betterproto.uint32_field(10)
    point_id: int = betterproto.uint32_field(12)