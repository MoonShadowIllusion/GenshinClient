# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonCandidateTeamPlayerLeaveNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .DungeonCandidateTeamPlayerLeaveReason import *


@dataclass
class DungeonCandidateTeamPlayerLeaveNotify(betterproto.Message):
    """
    CmdId: 926 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    reason: "DungeonCandidateTeamPlayerLeaveReason" = betterproto.enum_field(3)
    player_uid: int = betterproto.uint32_field(13)
