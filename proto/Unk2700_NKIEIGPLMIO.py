# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_NKIEIGPLMIO.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_NKIEIGPLMIO(betterproto.Message):
    """
    CmdId: 8459 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    challenge_type: int = betterproto.uint32_field(1)
    retcode: int = betterproto.int32_field(4)
    stage_id: int = betterproto.uint32_field(7)
