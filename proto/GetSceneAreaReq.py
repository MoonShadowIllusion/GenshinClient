# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GetSceneAreaReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class GetSceneAreaReq(betterproto.Message):
    """
    CmdId: 265 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    scene_id: int = betterproto.uint32_field(4)
    belong_uid: int = betterproto.uint32_field(7)