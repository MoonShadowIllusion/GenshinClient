# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ItemAddHintNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemHint import *
from .Vector import *


@dataclass
class ItemAddHintNotify(betterproto.Message):
    """
    CmdId: 607 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_position_valid: bool = betterproto.bool_field(14)
    quest_id: int = betterproto.uint32_field(3)
    reason: int = betterproto.uint32_field(6)
    is_general_reward_hiden: bool = betterproto.bool_field(15)
    item_list: List["ItemHint"] = betterproto.message_field(10)
    is_transfered_from_avatar_card: bool = betterproto.bool_field(12)
    position: "Vector" = betterproto.message_field(9)
    overflow_transformed_item_list: List["ItemHint"] = betterproto.message_field(8)
