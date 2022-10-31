# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BattlePassMission.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


class BattlePassMissionMissionStatus(betterproto.Enum):
    MISSION_STATUS_INVALID = 0
    MISSION_STATUS_UNFINISHED = 1
    MISSION_STATUS_FINISHED = 2
    MISSION_STATUS_POINT_TAKEN = 3


@dataclass
class BattlePassMission(betterproto.Message):
    cur_progress: int = betterproto.uint32_field(13)
    mission_status: "BattlePassMissionMissionStatus" = betterproto.enum_field(15)
    mission_id: int = betterproto.uint32_field(11)
    reward_battle_pass_point: int = betterproto.uint32_field(3)
    mission_type: int = betterproto.uint32_field(12)
    total_progress: int = betterproto.uint32_field(6)
