# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_GPHLCIAMDFG.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_GPHLCIAMDFG(betterproto.Message):
    """
    CmdId: 8095 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    schedule_id: int = betterproto.uint32_field(3)
    uid: int = betterproto.uint32_field(12)
