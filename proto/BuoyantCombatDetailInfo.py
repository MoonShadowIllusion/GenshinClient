# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BuoyantCombatDetailInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .BuoyantCombatDailyInfo import *


@dataclass
class BuoyantCombatDetailInfo(betterproto.Message):
    daily_info_list: List["BuoyantCombatDailyInfo"] = betterproto.message_field(8)