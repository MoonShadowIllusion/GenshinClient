# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SetUpAvatarTeamReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto


@dataclass
class SetUpAvatarTeamReq(betterproto.Message):
    """
    CmdId: 1690 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    team_id: int = betterproto.uint32_field(3)
    avatar_team_guid_list: List[int] = betterproto.uint64_field(7)
    cur_avatar_guid: int = betterproto.uint64_field(5)