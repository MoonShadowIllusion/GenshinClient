# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChangeMpTeamAvatarRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class ChangeMpTeamAvatarRsp(betterproto.Message):
    """
    CmdId: 1753 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(4)
    avatar_guid_list: List[int] = betterproto.uint64_field(3)
    cur_avatar_guid: int = betterproto.uint64_field(13)
