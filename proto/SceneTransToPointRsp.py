# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneTransToPointRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SceneTransToPointRsp(betterproto.Message):
    """
    CmdId: 253 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    point_id: int = betterproto.uint32_field(14)
    scene_id: int = betterproto.uint32_field(3)
    retcode: int = betterproto.int32_field(8)
