# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonCandidateTeamSetReadyRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DungeonCandidateTeamSetReadyRsp(betterproto.Message):
    """
    CmdId: 924 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(12)
