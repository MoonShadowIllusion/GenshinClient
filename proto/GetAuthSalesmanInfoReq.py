# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetAuthSalesmanInfoReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class GetAuthSalesmanInfoReq(betterproto.Message):
    """
    CmdId: 2070 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    schedule_id: int = betterproto.uint32_field(8)
