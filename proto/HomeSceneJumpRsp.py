# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HomeSceneJumpRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class HomeSceneJumpRsp(betterproto.Message):
    """
    CmdId: 4698 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(11)
    is_enter_room_scene: bool = betterproto.bool_field(8)