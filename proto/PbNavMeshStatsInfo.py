# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PbNavMeshStatsInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PbNavMeshStatsInfo(betterproto.Message):
    authority_ai_in_combat: int = betterproto.int32_field(10)
    no_authority_ai_in_combat: int = betterproto.int32_field(11)
    total_authority_ai: int = betterproto.int32_field(8)
    total_no_authority_ai: int = betterproto.int32_field(13)
