# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: RoguelikeSettleCoinInfo.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class RoguelikeSettleCoinInfo(betterproto.Message):
    coin_c: int = betterproto.uint32_field(8)
    coin_b: int = betterproto.uint32_field(10)
    cell_num: int = betterproto.uint32_field(1)
