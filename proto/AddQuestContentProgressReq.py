# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AddQuestContentProgressReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AddQuestContentProgressReq(betterproto.Message):
    """
    CmdId: 421 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    content_type: int = betterproto.uint32_field(6)
    param: int = betterproto.uint32_field(12)
    add_progress: int = betterproto.uint32_field(15)
