# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_IJLANPFECKC.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_IJLANPFECKC(betterproto.Message):
    """
    CmdId: 8277 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    stage_id: int = betterproto.uint32_field(9)
    challenge_id: int = betterproto.uint32_field(1)