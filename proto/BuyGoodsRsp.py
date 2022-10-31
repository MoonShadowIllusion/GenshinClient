# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BuyGoodsRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import List

import betterproto

from .ShopGoods import *


@dataclass
class BuyGoodsRsp(betterproto.Message):
    """
    CmdId: 735 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    buy_count: int = betterproto.uint32_field(14)
    goods: "ShopGoods" = betterproto.message_field(12)
    shop_type: int = betterproto.uint32_field(11)
    retcode: int = betterproto.int32_field(2)
    goods_list: List["ShopGoods"] = betterproto.message_field(5)
