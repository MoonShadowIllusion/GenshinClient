# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AISnapshotEntityData.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto

from .AISnapshotEntitySkillCycle import *


@dataclass
class AISnapshotEntityData(betterproto.Message):
    tick_time: float = betterproto.float_field(5)
    tactic: int = betterproto.uint32_field(2)
    finished_skill_cycles: List[
        "AISnapshotEntitySkillCycle"
    ] = betterproto.message_field(9)
    moved_distance: float = betterproto.float_field(4)
    ai_target_id: int = betterproto.uint32_field(13)
    threat_target_id: int = betterproto.uint32_field(3)
    threat_list_size: int = betterproto.uint32_field(1)
    entity_id: int = betterproto.uint32_field(15)
    hitting_avatars: Dict[int, int] = betterproto.map_field(
        7, betterproto.TYPE_UINT32, betterproto.TYPE_UINT32
    )
    distance_to_player: float = betterproto.float_field(11)
    attack_target_id: int = betterproto.uint32_field(10)
    real_time: float = betterproto.float_field(14)
