# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EnterWorldAreaReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class EnterWorldAreaReq(betterproto.Message):
    """
    CmdId: 250 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    area_type: int = betterproto.uint32_field(8)
    area_id: int = betterproto.uint32_field(1)