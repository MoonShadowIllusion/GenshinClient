# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonCandidateTeamRefuseNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DungeonCandidateTeamRefuseNotify(betterproto.Message):
    """
    CmdId: 988 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    player_uid: int = betterproto.uint32_field(3)
