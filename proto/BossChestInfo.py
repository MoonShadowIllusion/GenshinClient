# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BossChestInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import Dict, List

import betterproto

from .WeeklyBossResinDiscountInfo import *


@dataclass
class BossChestInfo(betterproto.Message):
    monster_config_id: int = betterproto.uint32_field(1)
    resin: int = betterproto.uint32_field(2)
    remain_uid_list: List[int] = betterproto.uint32_field(3)
    qualify_uid_list: List[int] = betterproto.uint32_field(4)
    uid_discount_map: Dict[int, "WeeklyBossResinDiscountInfo"] = betterproto.map_field(
        5, betterproto.TYPE_UINT32, betterproto.TYPE_MESSAGE
    )