# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EntityConfigHashEntry.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class EntityConfigHashEntry(betterproto.Message):
    job_id: int = betterproto.uint32_field(13)
    hash_value: int = betterproto.int32_field(6)
    entity_id: int = betterproto.uint32_field(11)