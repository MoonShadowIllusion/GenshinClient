# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FurnitureMakeStartReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class FurnitureMakeStartReq(betterproto.Message):
    """
    CmdId: 4633 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    avatar_id: int = betterproto.uint32_field(9)
    make_id: int = betterproto.uint32_field(1)