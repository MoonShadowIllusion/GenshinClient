# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: UnlockTransPointReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class UnlockTransPointReq(betterproto.Message):
    """
    CmdId: 3035 EnetChannelId: 0 EnetIsReliable: true IsAllowClient: true
    """

    point_id: int = betterproto.uint32_field(12)
    scene_id: int = betterproto.uint32_field(10)
