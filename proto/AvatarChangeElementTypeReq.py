# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarChangeElementTypeReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AvatarChangeElementTypeReq(betterproto.Message):
    """
    CmdId: 1785 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    scene_id: int = betterproto.uint32_field(7)
    area_id: int = betterproto.uint32_field(3)
