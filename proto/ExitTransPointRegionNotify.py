# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ExitTransPointRegionNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ExitTransPointRegionNotify(betterproto.Message):
    """
    CmdId: 282 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    point_id: int = betterproto.uint32_field(1)
    scene_id: int = betterproto.uint32_field(7)