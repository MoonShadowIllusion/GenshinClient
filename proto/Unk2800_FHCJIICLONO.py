# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2800_FHCJIICLONO.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2800_FHCJIICLONO(betterproto.Message):
    """
    CmdId: 21025 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    level_id: int = betterproto.uint32_field(9)
    retcode: int = betterproto.int32_field(2)