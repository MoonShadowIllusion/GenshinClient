# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneTransToPointReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SceneTransToPointReq(betterproto.Message):
    """
    CmdId: 239 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    scene_id: int = betterproto.uint32_field(13)
    point_id: int = betterproto.uint32_field(1)
