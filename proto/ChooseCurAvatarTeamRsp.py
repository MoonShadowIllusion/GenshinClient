# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChooseCurAvatarTeamRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ChooseCurAvatarTeamRsp(betterproto.Message):
    """
    CmdId: 1661 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    cur_team_id: int = betterproto.uint32_field(1)
    retcode: int = betterproto.int32_field(14)