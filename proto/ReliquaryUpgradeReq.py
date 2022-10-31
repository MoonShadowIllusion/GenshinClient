# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ReliquaryUpgradeReq.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class ReliquaryUpgradeReq(betterproto.Message):
    """
    CmdId: 604 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    item_param_list: List["ItemParam"] = betterproto.message_field(11)
    target_reliquary_guid: int = betterproto.uint64_field(6)
    food_reliquary_guid_list: List[int] = betterproto.uint64_field(12)
