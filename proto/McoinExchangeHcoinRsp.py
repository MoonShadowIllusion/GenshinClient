# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: McoinExchangeHcoinRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class McoinExchangeHcoinRsp(betterproto.Message):
    """
    CmdId: 687 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    mcoin_cost: int = betterproto.uint32_field(8)
    hcoin: int = betterproto.uint32_field(7)
    retcode: int = betterproto.int32_field(4)
