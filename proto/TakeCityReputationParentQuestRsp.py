# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TakeCityReputationParentQuestRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class TakeCityReputationParentQuestRsp(betterproto.Message):
    """
    CmdId: 2803 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(7)
    city_id: int = betterproto.uint32_field(14)
    parent_quest_list: List[int] = betterproto.uint32_field(9)
    item_list: List["ItemParam"] = betterproto.message_field(13)