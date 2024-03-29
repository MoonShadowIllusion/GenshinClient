# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: PersonalSceneJumpRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class PersonalSceneJumpRsp(betterproto.Message):
    """
    CmdId: 280 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    dest_scene_id: int = betterproto.uint32_field(5)
    retcode: int = betterproto.int32_field(8)
    dest_pos: "Vector" = betterproto.message_field(11)
