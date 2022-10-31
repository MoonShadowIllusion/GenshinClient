# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SumoSelectTeamAndEnterDungeonReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .SumoTeamData import *


@dataclass
class SumoSelectTeamAndEnterDungeonReq(betterproto.Message):
    """
    CmdId: 8215 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    activity_id: int = betterproto.uint32_field(1)
    stage_id: int = betterproto.uint32_field(7)
    difficulty_id: int = betterproto.uint32_field(4)
    team_list: List["SumoTeamData"] = betterproto.message_field(10)
