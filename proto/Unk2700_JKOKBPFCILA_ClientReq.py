# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_JKOKBPFCILA_ClientReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_JKOKBPFCILA_ClientReq(betterproto.Message):
    """
    CmdId: 467 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    quest_id: int = betterproto.uint32_field(4)
