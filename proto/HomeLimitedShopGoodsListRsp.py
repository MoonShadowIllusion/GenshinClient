# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeLimitedShopGoodsListRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .HomeLimitedShop import *


@dataclass
class HomeLimitedShopGoodsListRsp(betterproto.Message):
    """
    CmdId: 4546 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(6)
    shop: "HomeLimitedShop" = betterproto.message_field(12)
