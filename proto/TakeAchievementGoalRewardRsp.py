# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TakeAchievementGoalRewardRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class TakeAchievementGoalRewardRsp(betterproto.Message):
    """
    CmdId: 2681 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(15)
    id_list: List[int] = betterproto.uint32_field(12)
    item_list: List["ItemParam"] = betterproto.message_field(5)