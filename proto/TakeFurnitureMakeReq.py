# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: TakeFurnitureMakeReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class TakeFurnitureMakeReq(betterproto.Message):
    """
    CmdId: 4772 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    index: int = betterproto.uint32_field(8)
    is_fast_finish: bool = betterproto.bool_field(12)
    make_id: int = betterproto.uint32_field(7)
