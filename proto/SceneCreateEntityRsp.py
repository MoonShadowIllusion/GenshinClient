# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: SceneCreateEntityRsp.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .CreateEntityInfo import *


@dataclass
class SceneCreateEntityRsp(betterproto.Message):
    """
    CmdId: 226 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    retcode: int = betterproto.int32_field(14)
    entity_id: int = betterproto.uint32_field(1)
    entity: "CreateEntityInfo" = betterproto.message_field(10)
