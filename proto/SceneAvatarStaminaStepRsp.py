# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneAvatarStaminaStepRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class SceneAvatarStaminaStepRsp(betterproto.Message):
    """CmdId: 231 EnetChannelId: 0 EnetIsReliable: true IsAllowClient: true"""

    use_client_rot: bool = betterproto.bool_field(9)
    retcode: int = betterproto.int32_field(7)
    rot: "Vector" = betterproto.message_field(11)