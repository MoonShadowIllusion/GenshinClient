# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BargainOfferPriceReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class BargainOfferPriceReq(betterproto.Message):
    """
    CmdId: 493 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    bargain_id: int = betterproto.uint32_field(4)
    price: int = betterproto.uint32_field(6)
