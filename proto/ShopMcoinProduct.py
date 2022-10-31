# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ShopMcoinProduct.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ShopMcoinProduct(betterproto.Message):
    product_id: str = betterproto.string_field(1)
    price_tier: str = betterproto.string_field(2)
    mcoin_base: int = betterproto.uint32_field(3)
    mcoin_non_first: int = betterproto.uint32_field(4)
    mcoin_first: int = betterproto.uint32_field(5)
    bought_num: int = betterproto.uint32_field(6)
    is_audit: bool = betterproto.bool_field(7)