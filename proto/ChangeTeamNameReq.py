# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChangeTeamNameReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ChangeTeamNameReq(betterproto.Message):
    """
    CmdId: 1603 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    team_id: int = betterproto.int32_field(8)
    team_name: str = betterproto.string_field(9)
