# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_NJNMEFINDCF.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_NJNMEFINDCF(betterproto.Message):
    """
    CmdId: 8093 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(6)
    level_id: int = betterproto.uint32_field(1)
