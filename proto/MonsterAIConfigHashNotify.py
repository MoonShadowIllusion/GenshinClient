# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MonsterAIConfigHashNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MonsterAIConfigHashNotify(betterproto.Message):
    """
    CmdId: 3039 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    job_id: int = betterproto.uint32_field(10)
    entity_id: int = betterproto.uint32_field(15)
    hash_value: int = betterproto.int32_field(11)