# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: GuestPostEnterSceneNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class GuestPostEnterSceneNotify(betterproto.Message):
    """
    CmdId: 3144 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    scene_id: int = betterproto.uint32_field(5)
    uid: int = betterproto.uint32_field(4)