# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SumoSwitchTeamRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .SumoDungeonTeam import *


@dataclass
class SumoSwitchTeamRsp(betterproto.Message):
    """
    CmdId: 8525 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    next_valid_switch_time: int = betterproto.uint32_field(7)
    dungeon_team_list: List["SumoDungeonTeam"] = betterproto.message_field(10)
    activity_id: int = betterproto.uint32_field(6)
    retcode: int = betterproto.int32_field(14)
    cur_team_index: int = betterproto.uint32_field(11)
    stage_id: int = betterproto.uint32_field(5)
