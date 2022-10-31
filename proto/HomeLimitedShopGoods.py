# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeLimitedShopGoods.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class HomeLimitedShopGoods(betterproto.Message):
    buy_limit: int = betterproto.uint32_field(8)
    cost_item_list: List["ItemParam"] = betterproto.message_field(15)
    bought_num: int = betterproto.uint32_field(1)
    goods_item: "ItemParam" = betterproto.message_field(6)
    goods_id: int = betterproto.uint32_field(13)
    disable_type: int = betterproto.uint32_field(3)