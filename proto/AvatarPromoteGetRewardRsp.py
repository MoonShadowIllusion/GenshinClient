# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarPromoteGetRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AvatarPromoteGetRewardRsp(betterproto.Message):
    """
    CmdId: 1683 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(10)
    reward_id: int = betterproto.uint32_field(15)
    avatar_guid: int = betterproto.uint64_field(11)
    promote_level: int = betterproto.uint32_field(12)
