# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: MechanicusCandidateTeamCreateReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class MechanicusCandidateTeamCreateReq(betterproto.Message):
    """
    CmdId: 3981 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    difficult_level: int = betterproto.uint32_field(6)
