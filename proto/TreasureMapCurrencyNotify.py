# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TreasureMapCurrencyNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TreasureMapCurrencyNotify(betterproto.Message):
    """
    CmdId: 2171 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    currency_num: int = betterproto.uint32_field(8)