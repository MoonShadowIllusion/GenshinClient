# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EffigyChallengeDungeonResultInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class EffigyChallengeDungeonResultInfo(betterproto.Message):
    challenge_score: int = betterproto.uint32_field(7)
    is_in_time_limit: bool = betterproto.bool_field(8)
    challenge_id: int = betterproto.uint32_field(6)
    is_success: bool = betterproto.bool_field(15)
    challenge_max_score: int = betterproto.uint32_field(13)
