# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ArenaChallengeChildChallengeInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ArenaChallengeChildChallengeInfo(betterproto.Message):
    challenge_id: int = betterproto.uint32_field(12)
    challenge_type: int = betterproto.uint32_field(5)
    challenge_index: int = betterproto.uint32_field(4)
    is_success: bool = betterproto.bool_field(7)
    is_settled: bool = betterproto.bool_field(11)
