# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TowerMonthlyCombatRecord.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .TowerFightRecordPair import *


@dataclass
class TowerMonthlyCombatRecord(betterproto.Message):
    most_kill_avatar_pair: "TowerFightRecordPair" = betterproto.message_field(14)
    most_cast_normal_skill_avatar_pair: "TowerFightRecordPair" = (
        betterproto.message_field(8)
    )
    most_reveal_avatar_list: List["TowerFightRecordPair"] = betterproto.message_field(6)
    most_cast_energy_skill_avatar_pair: "TowerFightRecordPair" = (
        betterproto.message_field(4)
    )
    highest_dps_avatr_pair: "TowerFightRecordPair" = betterproto.message_field(12)
    most_take_damage_avatar_pair: "TowerFightRecordPair" = betterproto.message_field(9)