# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: FinishMainCoopReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class FinishMainCoopReq(betterproto.Message):
    """
    CmdId: 1952 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    id: int = betterproto.uint32_field(10)
    ending_save_point_id: int = betterproto.uint32_field(1)
