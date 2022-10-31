# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneCreateEntityReq.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .CreateEntityInfo import *
from .CreateReason import *


@dataclass
class SceneCreateEntityReq(betterproto.Message):
    """
    CmdId: 288 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    entity: "CreateEntityInfo" = betterproto.message_field(1)
    is_destroy_when_disconnect: bool = betterproto.bool_field(10)
    reason: "CreateReason" = betterproto.enum_field(3)