# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneTimeNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SceneTimeNotify(betterproto.Message):
    """
    CmdId: 245 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    scene_time: int = betterproto.uint64_field(14)
    is_paused: bool = betterproto.bool_field(1)
    scene_id: int = betterproto.uint32_field(7)