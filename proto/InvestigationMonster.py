# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: InvestigationMonster.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *
from .WeeklyBossResinDiscountInfo import *


class InvestigationMonsterLockState(betterproto.Enum):
    LOCK_STATE_NONE = 0
    LOCK_STATE_QUEST = 1


@dataclass
class InvestigationMonster(betterproto.Message):
    is_alive: bool = betterproto.bool_field(9)
    refresh_interval: int = betterproto.uint32_field(3)
    id: int = betterproto.uint32_field(13)
    level: int = betterproto.uint32_field(5)
    boss_chest_num: int = betterproto.uint32_field(1)
    weekly_boss_resin_discount_info: "WeeklyBossResinDiscountInfo" = (
        betterproto.message_field(12)
    )
    monster_id: int = betterproto.uint32_field(301)
    pos: "Vector" = betterproto.message_field(14)
    resin: int = betterproto.uint32_field(8)
    max_boss_chest_num: int = betterproto.uint32_field(4)
    next_refresh_time: int = betterproto.uint32_field(11)
    group_id: int = betterproto.uint32_field(285)
    scene_id: int = betterproto.uint32_field(10)
    is_area_locked: bool = betterproto.bool_field(15)
    lock_state: "InvestigationMonsterLockState" = betterproto.enum_field(2)
    next_boss_chest_refresh_time: int = betterproto.uint32_field(7)
    city_id: int = betterproto.uint32_field(6)