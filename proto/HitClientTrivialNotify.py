# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: HitClientTrivialNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class HitClientTrivialNotify(betterproto.Message):
    """
    CmdId: 244 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    position: "Vector" = betterproto.message_field(11)
    owner_entity_id: int = betterproto.uint32_field(12)
