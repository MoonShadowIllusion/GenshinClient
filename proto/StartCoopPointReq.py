# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: StartCoopPointReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class StartCoopPointReq(betterproto.Message):
    """
    CmdId: 1992 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    coop_point: int = betterproto.uint32_field(7)
