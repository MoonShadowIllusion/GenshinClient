# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk3000_JIEPEGAHDNH.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk3000_JIEPEGAHDNH(betterproto.Message):
    """
    CmdId: 24152 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    level_id: int = betterproto.uint32_field(1)
    retcode: int = betterproto.int32_field(8)
