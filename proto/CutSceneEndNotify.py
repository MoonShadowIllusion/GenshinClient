# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: CutSceneEndNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class CutSceneEndNotify(betterproto.Message):
    """
    CmdId: 215 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(5)
    cutscene_id: int = betterproto.uint32_field(14)