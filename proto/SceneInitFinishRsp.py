# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneInitFinishRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class SceneInitFinishRsp(betterproto.Message):
    """
    CmdId: 207 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(13)
    enter_scene_token: int = betterproto.uint32_field(8)
