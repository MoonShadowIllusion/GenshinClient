# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PlayerRechargeDataNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ProductPriceTier import *


@dataclass
class PlayerRechargeDataNotify(betterproto.Message):
    """
    CmdId: 4102 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    card_product_remain_days: int = betterproto.uint32_field(12)
    product_price_tier_list: List["ProductPriceTier"] = betterproto.message_field(11)
