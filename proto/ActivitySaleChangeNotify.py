# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ActivitySaleChangeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ActivitySaleChangeNotify(betterproto.Message):
    """
    CmdId: 2071 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    sale_id: int = betterproto.uint32_field(5)
    is_close: bool = betterproto.bool_field(1)