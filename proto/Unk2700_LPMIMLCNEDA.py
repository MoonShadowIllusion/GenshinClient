# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_LPMIMLCNEDA.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_LPMIMLCNEDA(betterproto.Message):
    """
    CmdId: 8518 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    stage_id: int = betterproto.uint32_field(2)
    challenge_id: int = betterproto.uint32_field(7)
