# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonCandidateTeamCreateRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DungeonCandidateTeamCreateRsp(betterproto.Message):
    """
    CmdId: 906 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(1)
