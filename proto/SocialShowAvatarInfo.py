# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SocialShowAvatarInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SocialShowAvatarInfo(betterproto.Message):
    avatar_id: int = betterproto.uint32_field(1)
    level: int = betterproto.uint32_field(2)
    costume_id: int = betterproto.uint32_field(3)
