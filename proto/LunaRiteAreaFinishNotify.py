# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: LunaRiteAreaFinishNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class LunaRiteAreaFinishNotify(betterproto.Message):
    """
    CmdId: 8213 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    area_id: int = betterproto.uint32_field(2)
