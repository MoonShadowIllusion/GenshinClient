# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ChangeTeamNameRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ChangeTeamNameRsp(betterproto.Message):
    """
    CmdId: 1666 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(11)
    team_name: str = betterproto.string_field(2)
    team_id: int = betterproto.int32_field(4)
