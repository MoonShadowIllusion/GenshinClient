# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: DungeonCandidateTeamReplyInviteReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class DungeonCandidateTeamReplyInviteReq(betterproto.Message):
    """
    CmdId: 941 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_accept: bool = betterproto.bool_field(5)
