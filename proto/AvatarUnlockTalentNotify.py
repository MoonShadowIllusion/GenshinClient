# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarUnlockTalentNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AvatarUnlockTalentNotify(betterproto.Message):
    """
    CmdId: 1012 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity_id: int = betterproto.uint32_field(14)
    avatar_guid: int = betterproto.uint64_field(13)
    talent_id: int = betterproto.uint32_field(10)
    skill_depot_id: int = betterproto.uint32_field(1)