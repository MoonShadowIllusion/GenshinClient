# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BattlePassAllDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .BattlePassMission import *
from .BattlePassSchedule import *


@dataclass
class BattlePassAllDataNotify(betterproto.Message):
    """
    CmdId: 2626 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    have_cur_schedule: bool = betterproto.bool_field(2)
    mission_list: List["BattlePassMission"] = betterproto.message_field(4)
    cur_schedule: "BattlePassSchedule" = betterproto.message_field(1)
