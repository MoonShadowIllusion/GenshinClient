# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ShopGoods.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ItemParam import *


@dataclass
class ShopGoods(betterproto.Message):
    discount_end_time: int = betterproto.uint32_field(258)
    min_level: int = betterproto.uint32_field(8)
    end_time: int = betterproto.uint32_field(11)
    cost_item_list: List["ItemParam"] = betterproto.message_field(3)
    secondary_sheet_id: int = betterproto.uint32_field(318)
    hcoin: int = betterproto.uint32_field(1)
    mcoin: int = betterproto.uint32_field(14)
    discount_id: int = betterproto.uint32_field(1998)
    single_limit: int = betterproto.uint32_field(247)
    goods_id: int = betterproto.uint32_field(13)
    next_refresh_time: int = betterproto.uint32_field(7)
    max_level: int = betterproto.uint32_field(4)
    disable_type: int = betterproto.uint32_field(6)
    discount_begin_time: int = betterproto.uint32_field(574)
    pre_goods_id_list: List[int] = betterproto.uint32_field(2)
    begin_time: int = betterproto.uint32_field(5)
    scoin: int = betterproto.uint32_field(15)
    bought_num: int = betterproto.uint32_field(10)
    buy_limit: int = betterproto.uint32_field(12)
    goods_item: "ItemParam" = betterproto.message_field(9)
