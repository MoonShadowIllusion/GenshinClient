# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: Unk2700_AEEMJIMOPKD.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class Unk2700_AEEMJIMOPKD(betterproto.Message):
    """
    CmdId: 8481 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    stage_id: int = betterproto.uint32_field(13)
    retcode: int = betterproto.int32_field(14)
    is_success: bool = betterproto.bool_field(3)
