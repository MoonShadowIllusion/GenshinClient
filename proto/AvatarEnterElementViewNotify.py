# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: AvatarEnterElementViewNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto


@dataclass
class AvatarEnterElementViewNotify(betterproto.Message):
    """
    CmdId: 334 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    is_triggerd: bool = betterproto.bool_field(3)
    avatar_entity_id: int = betterproto.uint32_field(12)