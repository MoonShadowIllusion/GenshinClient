# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonCandidateTeamKickRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DungeonCandidateTeamKickRsp(betterproto.Message):
    """
    CmdId: 974 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(1)
