# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarSkillUpgradeRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AvatarSkillUpgradeRsp(betterproto.Message):
    """
    CmdId: 1048 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_guid: int = betterproto.uint64_field(11)
    cur_level: int = betterproto.uint32_field(14)
    avatar_skill_id: int = betterproto.uint32_field(9)
    old_level: int = betterproto.uint32_field(3)
    retcode: int = betterproto.int32_field(4)
