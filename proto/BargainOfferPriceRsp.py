# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: BargainOfferPriceRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .BargainResultType import *


@dataclass
class BargainOfferPriceRsp(betterproto.Message):
    """
    CmdId: 427 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(5)
    result_param: int = betterproto.uint32_field(13)
    bargain_result: "BargainResultType" = betterproto.enum_field(14)
    cur_mood: int = betterproto.int32_field(6)
