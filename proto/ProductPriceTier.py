# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ProductPriceTier.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ProductPriceTier(betterproto.Message):
    product_id: str = betterproto.string_field(6)
    price_tier: str = betterproto.string_field(12)
