# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChannelerSlabAssistInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ChannelerSlabAssistInfo(betterproto.Message):
    uid: int = betterproto.uint32_field(10)
    avatar_level: int = betterproto.uint32_field(12)
    avatar_id: int = betterproto.uint32_field(6)
