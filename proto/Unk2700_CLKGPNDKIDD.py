# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_CLKGPNDKIDD.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_CLKGPNDKIDD(betterproto.Message):
    """
    CmdId: 8725 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    schedule_id: int = betterproto.uint32_field(8)
