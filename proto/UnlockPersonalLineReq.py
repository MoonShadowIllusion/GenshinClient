# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: UnlockPersonalLineReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class UnlockPersonalLineReq(betterproto.Message):
    """
    CmdId: 449 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    personal_line_id: int = betterproto.uint32_field(4)
