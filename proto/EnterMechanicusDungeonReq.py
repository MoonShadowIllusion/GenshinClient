# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EnterMechanicusDungeonReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class EnterMechanicusDungeonReq(betterproto.Message):
    """
    CmdId: 3931 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    difficult_level: int = betterproto.uint32_field(7)