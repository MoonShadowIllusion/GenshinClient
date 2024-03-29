# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BattlePassBuySuccNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class BattlePassBuySuccNotify(betterproto.Message):
    """
    CmdId: 2614 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    schedule_id: int = betterproto.uint32_field(4)
    product_play_type: int = betterproto.uint32_field(11)
    add_point: int = betterproto.uint32_field(12)
    item_list: List["ItemParam"] = betterproto.message_field(9)
