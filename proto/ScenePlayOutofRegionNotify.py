# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: ScenePlayOutofRegionNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class ScenePlayOutofRegionNotify(betterproto.Message):
    """
    CmdId: 4355 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    play_id: int = betterproto.uint32_field(13)
