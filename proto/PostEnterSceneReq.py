# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PostEnterSceneReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class PostEnterSceneReq(betterproto.Message):
    """
    CmdId: 3312 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    enter_scene_token: int = betterproto.uint32_field(12)
