# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: EvtAvatarSitDownNotify.proto
# plugin: python-betterproto
from dataclasses import dataclass

import betterproto

from .Vector import *


@dataclass
class EvtAvatarSitDownNotify(betterproto.Message):
    """
    CmdId: 324 EnetChannelId: 0 EnetIsReliable: false IsAllowClient: true
    """

    position: "Vector" = betterproto.message_field(9)
    entity_id: int = betterproto.uint32_field(4)
    chair_id: int = betterproto.uint64_field(6)