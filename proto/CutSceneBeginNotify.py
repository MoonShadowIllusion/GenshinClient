# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CutSceneBeginNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class CutSceneBeginNotify(betterproto.Message):
    """
    CmdId: 296 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    cutscene_id: int = betterproto.uint32_field(14)
    is_wait_others: bool = betterproto.bool_field(9)
