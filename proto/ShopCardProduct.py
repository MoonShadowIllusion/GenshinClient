# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ShopCardProduct.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class ShopCardProduct(betterproto.Message):
    product_id: str = betterproto.string_field(1)
    price_tier: str = betterproto.string_field(2)
    mcoin_base: int = betterproto.uint32_field(3)
    hcoin_per_day: int = betterproto.uint32_field(4)
    days: int = betterproto.uint32_field(5)
    remain_reward_days: int = betterproto.uint32_field(6)
    card_product_type: int = betterproto.uint32_field(7)
    resin_card: "ShopCardProductResinCard" = betterproto.message_field(
        101, group="extra_card_data"
    )


@dataclass
class ShopCardProductResinCard(betterproto.Message):
    base_item_list: List["ItemParam"] = betterproto.message_field(1)
    per_day_item_list: List["ItemParam"] = betterproto.message_field(2)