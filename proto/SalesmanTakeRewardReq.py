# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SalesmanTakeRewardReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SalesmanTakeRewardReq(betterproto.Message):
    """
    CmdId: 2191 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    position: int = betterproto.uint32_field(8)
    schedule_id: int = betterproto.uint32_field(7)